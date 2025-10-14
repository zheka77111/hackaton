import asyncio
from datetime import datetime
import os
import pickle
import subprocess
from typing import Any, cast

from dotenv import find_dotenv, load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables.config import RunnableConfig
from langchain_core.tools import tool
from langchain_gigachat import GigaChat
from langchain_ollama import ChatOllama
from loguru import logger
from func.plan import PentestArtifacts
from pydantic import BaseModel
from langchain_tavily import TavilySearch
from blanks.prompts import extract_prompt
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_gigachat.embeddings import GigaChatEmbeddings

load_dotenv(find_dotenv())
ip = os.environ.get('IP', 'localhost')

# Assuming 'model' is a GigaChat instance, defined somewhere globally
# For example:
# model = GigaChat(credentials=os.environ.get("GIGACHAT_CREDENTIALS"), verify_ssl_certs=False)


from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
key = os.environ.get('GIGACHAT_API_KEY')

console_log = os.environ.get('CONSOLE_LOG_FILE', 'logs/my_console.md')
report_file = str(os.environ.get('LOG_FILE', 'report_task_1.md'))


embeddings = GigaChatEmbeddings(credentials=key, 
								scope='GIGACHAT_API_CORP',
								verify_ssl_certs=False)
persist_dir = "my_chroma_store"
vectorstore = Chroma(persist_directory=persist_dir,
                     embedding_function=embeddings)


class Answer(BaseModel):
    "относиться ли ответ к текущей задаче"
    answer: bool


def extract_pentest_artifacts(	output: str, 
							  	# task: str,
								) -> PentestArtifacts:
	"""
	Использует LLM для структурированного извлечения credentials, endpoints и т.д. из вывода команды.
	
	Args:
	output: str - вывод консоли после выполнения

	"""

	config = RunnableConfig(configurable={"thread_id": "extract"})
	model = GigaChat(credentials=key,
				model='GigaChat-2-Max',
				scope='GIGACHAT_API_CORP',
				temperature = 0,
				verify_ssl_certs = False,
				profanity_check=False
				)
	structured_model = model.with_structured_output(PentestArtifacts)
	response = structured_model.invoke([
						SystemMessage(extract_prompt.format(ip=ip)),
						HumanMessage(output)
					], 
					config=config
				)
	# check_model = model.with_structured_output(Answer)

	# check = check_model.invoke([
    #                 SystemMessage("Ты критик. Оцени, относиться ли данная информация <info> к задаче <task>." 
    #                               f"особое внимание обрати на то, что ip адрес должен совпадать с {ip}" )
    #                 ,
    #                 HumanMessage(f"<info>: {response}"
    #                             f"<task>: {task}")
    #             ])
	
	# check = cast(Answer, check) 


	# logger.debug(response)
	# logger.debug(check)

	return response #if check.answer else PentestArtifacts()


@tool
def mem_tool(query: str, k: int = 10, ):
	"""Search in memory for pentest artifacts
	Args
	query: str Запрос в виде строки, информация, которую нужно найти.
	k: int Количество возвращаемых результатов
	"""
	
	return vectorstore.similarity_search(query, k=10)


@tool
def get_pentest_artifact(is_all:bool) -> PentestArtifacts:
	"""Проверить хранилище данных о пентесте для получения информации.
	Args:
	s_all:bool - провести сбор из вывода консоли в хранилище данных, True после 10 вызовов tool get_shell_output для 
	периодического обновления данных.
	"""
	# global pentest_store
	pentest_store = PentestArtifacts()
	if not is_all:
		if os.path.exists('pentest_dump.pkl'):
			with open('pentest_dump.pkl', 'rb') as file:
				pentest_store = pickle.load(file)
				logger.debug("load from dump: " + str(pentest_store.model_dump()))
				return pentest_store
	else:

		pentest_store = PentestArtifacts()
		logger.debug("created new pentest_store")
		with open(report_file, "r") as file, open(console_log, "r") as file1, open("pentest_dump.pkl","wb") as dump:
			text = file.readlines()
			res = extract_pentest_artifacts('\n'.join(text))
			logger.debug(res)
			pentest_store.increment(res)

			text1 = file1.readlines()
			if len(text1) < 11:

				res = extract_pentest_artifacts('\n'.join(text1))
				pentest_store.increment(res)	
				logger.debug(res)
			else:
				for i in range(len(text1) // 10):
					# print(text[i*100:(i+1)*100])
					res = extract_pentest_artifacts('\n'.join(text1[i*10:(i+1)*10]))
					logger.debug(res)
					pentest_store.increment(res)	
			
			pickle.dump(pentest_store, dump)
			logger.debug(f"read from file {report_file}: " + str(pentest_store.model_dump()))
			logger.debug(f"read from file {console_log}: " + str(pentest_store.model_dump()))

		return pentest_store


@tool
def get_shell_output(command: str,   pentest_store:PentestArtifacts, timeout: int = 500) -> str:
	"""Run shell command and program to find files, pentest like john, sqlmap, curl etc.
	Args 
	command: str - bash command for kali linux terminal
	task: str - текущая задача
	pentest_store:PentestArtifacts - хранилище данных
	timeout: int - timeout to command
	"""
	# pentest_store = PentestArtifacts()
	if not command:
		raise ValueError("Input is empty")
	if not isinstance(command, str):
		raise ValueError("Input is not a string")
	logger.debug(f"{command =}, {timeout =}")
	result = subprocess.run(
				args= command,
				shell=True,
				capture_output=True,
				text=True,
				timeout=timeout
			)
	output = result.stdout
	logger.debug(f"{output =}")
	if output !='':
		artifacts = extract_pentest_artifacts(output)
		# for  artifacts.
		# store.put("pentest", "artifacts")
		pentest_store.increment(artifacts)
		with open(console_log,"a") as file:
			file.write(artifacts.model_dump_json())
			file.write(f'{{"command": "{command}", "result": "{result.stdout}"}}')
		logger.debug(f"{artifacts =}")
		vectorstore.add_documents([Document(
        page_content=result.stdout,
        metadata={"command": command, 
				  "error":result.stderr,
				  "timestamp": datetime.now().isoformat(),
				  "artifacts": artifacts.model_dump_json()}
    								)])
		res = {
		"command_history": 
		
		[{
			"command": command,
			"output": result.stdout,
			"error":result.stderr,
			"timestamp": datetime.now().isoformat()
		}],
		"found_credentials": artifacts.credentials,
		"found_endpoints": artifacts.endpoints,
		"found_services": artifacts.services,
		"found_cookies": artifacts.cookies,
		"found_vulns": artifacts.vulnerabilities
		
	}
		logger.debug(res)
	if result.returncode != 0:
		raise ValueError(f"Command {command} failed with error {result.stderr}")
	
	
	return result.stdout


tavily_search_tool = TavilySearch(
				max_results=3,
				include_answer=True,
				include_raw_content=True,
				include_images=False,
				# search_depth="advanced",
				# include_domains = []
				# exclude_domains = []
			)


# client = MultiServerMCPClient(
#         connections={
#             "plan": {
#                 "url": "https://server.smithery.ai/@ibrahimsaleem/pentestthinkingmcp/mcp?api_key=438f803f-29cf-4664-8912-e6080f1397d5&profile=surprised-asp-jL1xbY",
#                 "transport": "streamable_http",
#             }
#         } # type: ignore
#     )
# async def planning():
# 	return await client.get_tools()

