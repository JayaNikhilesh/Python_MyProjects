import os

from crewai_tools import FileReadTool
from crewai import Agent
from crewai.llm import LLM

from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model=os.getenv("model"),
    api_key=os.getenv("OR_API"),
    base_url=os.getenv("base_url"),
)

File_Read_Tool = FileReadTool(file_path="transcript.txt", encoding="utf-8")

#Agent - It will read the transcript file and give us summarized data
summarizer = Agent(
    role="Transcript summarizer",
    goal="Read the transcript.txt file and gives us summary, important decisions, dead lined mentioned",
    llm=llm,
    backstory=""" You are a very good at giving summary. You always take all the most important details from a 
    transcript and gives important details. You also summarized 1000's of transcripts and have very good 
    experience in it.""",
    tools=[File_Read_Tool],
    verbose=True,
    respect_context_window=True,
    max_iter=1,
    max_execution_time=150,
    max_rpm=3,
)
