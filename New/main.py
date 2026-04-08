import os
import json
from crewai import Process, Crew

from tasks import researcher_task, writer_task, editor_task

from agents import researcher, writer, editor

devops_crew = Crew(
    agents = [researcher, writer, editor],
    tasks = [researcher_task, writer_task, editor_task],
    verbose = True,
    tracing=True,
    process=Process.sequential,
    catch=True,
    max_rpm=15,
)

if __name__ == "__main__":
    print("AI Agents are starting to look for keywords and articles from websearch")
    topic = input("Enter the topic or keyword you want me to search: ")

    result=devops_crew.kickoff(
        inputs = {"topic":topic}
    )
    print(result)