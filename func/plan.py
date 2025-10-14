from typing import Any, Dict
from typing import Literal, TypedDict, List
from langchain_core.messages import BaseMessage

from pydantic import BaseModel, Field, model_validator


class PlanStep(BaseModel):
	id: str
	name: str
	status: Literal["pending", "in_progress", "completed", "failed", "skipped"]
	retry_count: int = 0
	max_retries: int = 2
	agent_type: str
	alternative_strategies: List[str]



class Credential(BaseModel):
	type: str = Field(..., description="Тип найденных credentials (например, password, token, key)")
	login: str = Field(..., description="Значение логина, например admin, user  и др.")
	password: str = Field(..., description="Значение password credentials")
	context: str = Field("", description="Контекст, где найдено, к какому сервису относится, например ssh//admin:passwod")

	
class PentestArtifacts(BaseModel):
	"""
	Structured data extracted from pentest outputs, including credentials, endpoints, etc.
	"""


	credentials: List[Credential]  = Field(default_factory=list, description="Найденные credentials, обязательно указать логин")
	endpoints: List[str] = Field(default_factory=list, description="Найденные endpoints (url, ip, порты)")
	services:  List[str] = Field(default_factory=list, description="Найденные сервисы, их версии, например OpenSSH 8.9p1 Ubuntu 3ubuntu0.13:22(port number) или vsftpd 2.3.4:212")
	cookies: List[str] = Field(default_factory=list, description="Найденные cookies с указанием сервиса и страницы endpoints")
	vulnerabilities: List[str] = Field(default_factory=list, description="Найденные уязвимости в нотации CVE или CWE")

	def increment(self, other: 'PentestArtifacts') -> None:
		if other is None:
			return
		# Добавляем unique credentials
		if other.credentials is not None:
			for cred in other.credentials:
				if cred not in self.credentials:
					self.credentials.append(cred)
		
		# Добавляем unique endpoints
		if other.endpoints is not None:
			for endpoint in other.endpoints:
				if endpoint not in self.endpoints:
					self.endpoints.append(endpoint)
					
			# Добавляем unique cookies
		if other.services is not None:
			for service in other.services:
				if service not in self.services:
					self.services.append(service)

		if other.cookies is not None:
			for cookie in other.cookies:
				if cookie not in self.cookies:
					self.cookies.append(cookie)
				
		# Добавляем unique vulnerabilities
		if other.vulnerabilities is not None:

			for vuln in other.vulnerabilities:
				if vuln not in self.vulnerabilities:
					self.vulnerabilities.append(vuln)



class PlanningEngine(BaseModel):
	messages: List[BaseMessage]  # or List[BaseMessage] if you have a message class
	remaining_steps: int
	def generate_initial_plan(self, target_info: Dict[str, Any]) -> List[PlanStep]:
		
		return [
			PlanStep(id="1", name="Network Discovery",status="pending", agent_type="NmapAgent", alternative_strategies=["get info from database", "get info from web service"]),
			PlanStep(id="2", name="Vulnerability Assessment", status="pending", agent_type="MetasploitAgent", alternative_strategies=["get info from database", "get info from web service"]),
			PlanStep(id="3", name="Credential Attacks", status="pending", agent_type="BruteForceAgent", alternative_strategies=["get info from database", "get info from web service"])
		]


class PentestState(TypedDict):
	plan: List[PlanStep]
	current_step: int
	artifacts: PentestArtifacts
	metrics: Dict[str, Any]


	