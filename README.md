This project is a sophisticated, multi-agent penetration testing framework built with Python, LangChain, and LangGraph. It automates security vulnerability discovery using a team of specialized AI agents orchestrated by a central "supervisor."

Key components include:

*   **AI Agents:**
    *   `shell_agent`: Executes shell commands for pentesting.
    *   `research_agent`: Conducts web research on vulnerabilities.
    *   `critique_agent`: Advises and critiques the pentesting process.
    *   `planing_agent`: Develops the pentesting plan by using MCP server, but not used this time.

*   **Tools:**
    *   Shell command execution.
    *   Web search (Tavily).
    *   Pentesting artifact management (credentials, endpoints, etc.).

*   **Workflows:**
    *   A main workflow for executing the pentest.
    *   A planning workflow for creating the attack plan.

*   **Files:**
    *  task1.ipynb - 1 task solving.
    *  task2.ipynb - 2 task solving.
    *  task3.ipynb - 3 task solving.
    *  task4.ipynb - 4 task solving.
    *  blanks/prompts.py - prompt for agents (not all had been used).
    *  func/methods_1.py - methods and tools for agents (not all had been used).
    * task3_files/* - filse for Sast task.
    * logs/ - log files
    * logs/report_task_1.md - 1 task solving report.
    * logs/report_task_4.md - 4 task solving report.

    



The project uses GigaChat and OpenAI models.

However, the project appears to be incomplete:

*   The main entrypoint (`main.py`) is a placeholder and doesn't run the pentesting logic.
*   There are missing imports and undefined variables in the core logic file (`graph/solver.py`), which will prevent it from running as-is.

This comand to run kali linux docker container to execute comand.
docker run -it --privileged --name hackathon_eval -v /Users/zheka/Documents/ML/agents/hackaton/hackaton-app:/app -p 3000:3000 -rm  hackathon:v_3
