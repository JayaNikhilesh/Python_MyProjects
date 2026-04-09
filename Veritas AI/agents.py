import os

from crewai import Agent
from crewai.llm import LLM

from dotenv import load_dotenv
load_dotenv()

from tools import EXASearchTool, document_writer_tool, content_refiner_tool


llm = LLM(
    model=os.getenv("model"),
    api_key=os.getenv("OR_API"),
    base_url="https://openrouter.ai/api/v1"
)

#Agent1 doing research on top trending keywords and articles
researcher = Agent(
    role="Online summarizer",
    goal="Researcher for top trending keywords and articles in EXASearchTool",
    llm=llm,
    backstory=""" You are a top web summarizer always looking for top articles in the internet oe EXASearchTool.
    you have 15 years of experience in looking for top trending articles and keywords.""",
    tools=[EXASearchTool],
    verbose=True,
    respect_context_window=True,
    max_iter=1,
    max_execution_time=150,
    max_rpm=5,
)

#Agent2 He will write the blog post on keywords or articles send by the Agent1
writer = Agent(
    role="Write blogs on trending keywords and articles",
    goal="Writing blogs on top keywords and articles send by Agent1",
    llm=llm,
    backstory="""You are a writer with 25 years of experience who writes blogs
     that make the customers to read even if they are not interested.
     Your blogs make the customers read other blogs of you one after another.
     your blogs contain official information and important information on that article in the shortest matter.
     """,
    tools=[document_writer_tool],
    verbose=True,
    respect_context_window=True,
    max_iter=1,
    max_execution_time=300,
    max_rpm=2,
)

#Agent3 He will optimize the blogs written by Agent2 and make it ready for uploading
editor = Agent(
    role="Context editor",
    goal="Make the blogs more refined and presentable for reading",
    llm=llm,
    backstory="""You are a Context editor with 15 years of experience.
    You make wonderful titles for the context that makes all the humans to take a look into it.
    You will improve keyword density, adding meta descriptions, and scoring readability.""",
    tools=[document_writer_tool,content_refiner_tool],
    verbose=True,
    respect_context_window=True,
    max_iter=1,
    max_execution_time=150,
    max_rpm=5,
)
