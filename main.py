from dotenv import load_dotenv
load_dotenv()

from helpers.format_news_for_email import format_news_for_email
from helpers.is_valid_email import is_valid_email

import os
import json
from datetime import datetime

from crewai import Agent, Crew, Task, Process
from crewai_tools import ScrapeWebsiteTool
import yaml
from helpers.replace_yaml_variables import replace_yaml_variables
from application_schema.news_results import NewsResults

from helpers.send_email import send_email

import agentops
agentops.init(os.getenv("AGENTOPS_API_KEY"))

emails=(os.getenv("COMMA_SEPARATED_EMAILS") or "")

# vvv YAML Configuration vvv
current_date = datetime.now().strftime("%Y-%m-%d") # Include current date for context
replacements = {
    "current_date": current_date
}
tasks_yaml = None
with open("config/tasks.yaml", 'r') as file:
    tasks_yaml = yaml.safe_load(file)
    tasks_yaml = replace_yaml_variables(tasks_yaml, replacements)
agents_yaml = None
with open("config/agents.yaml", 'r') as file:
    agents_yaml = yaml.safe_load(file)

scrape_web_tool = ScrapeWebsiteTool()

def main():
    manager = Agent(
        role=agents_yaml["manager"]["role"],
        goal=agents_yaml["manager"]["goal"],
        backstory=agents_yaml["manager"]["backstory"],
        verbose=True,
    )

    workers = []

    for worker in agents_yaml["workers"]:
        workers.append(
            Agent(
                role=agents_yaml["workers"][worker]["role"],
                goal=agents_yaml["workers"][worker]["goal"],
                backstory=agents_yaml["workers"][worker]["backstory"],
                verbose=True,
                tools=[scrape_web_tool],
            )
        )

    research_task = Task(
        description=tasks_yaml["research_task"]["description"],
        expected_output=tasks_yaml["research_task"]["expected_output"],
        output_pydantic=NewsResults,
        output_file='report.json'
    )

    crew = Crew(
        agents=workers,
        manager_agent=manager,
        tasks=[research_task],
        process=Process.hierarchical,
        verbose=True,
    )

    crew_output = crew.kickoff()

    print('FINAL OUTPUT')
    print(crew_output.raw)

    email_list = emails.split(",")
    for email in email_list:
        if bool(email) and is_valid_email(email):
            send_email([email.strip()], format_news_for_email(crew_output.pydantic, current_date))

    
    
if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        message = (
            f"Attempt failed: {str(err)}"
        )
        print(json.dumps({"message": message, "severity": "ERROR"}))
