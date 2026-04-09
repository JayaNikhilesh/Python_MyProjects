import os
import json
from crewai import Crew, Agent, Task

from tasks import summarizer_task
from crewai_tools import FileReadTool

from agents import summarizer

File_Read_Tool = FileReadTool()

devops_crew = Crew(
    agents = [summarizer],
    tasks = [summarizer_task],
    verbose = True,
    tracing=True,
    catch=True,
    max_rpm=15,
)

if __name__ == "__main__":
    print("AI Agents are starting to summarise the transcript")

    result = devops_crew.kickoff()
    print("\n--- Meeting Summary ---\n")
    print(result)

output_data = json.dumps(result, ensure_ascii=False, indent=4)

output_data = {"summary": str(result)}
with open("tasks_outputs/summary.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

print("The summary is saved in json file")