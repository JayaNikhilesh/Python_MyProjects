import os

from crewai.tools import BaseTool
from crewai_tools import EXASearchTool
from dotenv import load_dotenv
load_dotenv()


EXA_API_KEY = os.getenv("EXA_API_KEY")
EXASearchTool=EXASearchTool()

#Create a tool for printing the data in ba JSON file

class DocumentWriterTool(BaseTool):
    name: str = "DocumentWriterTool"
    description: str = "Formats text into structured JSON or Markdown"

    def _run(self, text: str) -> str:
        return f"{{'document': '{text}'}}"

class ContentRefinerTool(BaseTool):
    name: str = "ContentRefinerTool"
    description: str = "Cleans and refines raw content for clarity and readability."

    def _run(self, text: str) -> str:
        # Example: basic refinement — strip whitespace and capitalize
        refined = text.strip().capitalize()
        return refined

document_writer_tool=DocumentWriterTool()
content_refiner_tool=ContentRefinerTool()