import os

from crewai import Task


from agents import summarizer

os.makedirs("tasks_outputs", exist_ok=True)

#Task Collect the data from transcript.txt and gives a detailed summary and tells important decisions.
summarizer_task=Task(
    description="""Summarise the data from transcript.txt using FileReadTool
    
    your summary should contain:
    1.Summary of the data in transcript.txt
    2.Should give the information about the important decisions taken in the meeting
    3.Should give the deadline times given in the transcript.txt
    4.Should give action items with their owners
    5.It should give all the questions talked in the meeting at the last of the summary
    6.Hide the sensitive information
    7.Should not give the information outside the transcript
    8.It should be easy to understand
    9.Give the data in multiple sections. All the information about a single topic in one section
    
    Focus on summarising the data from transcript.txt without loosing important data""",
    expected_output="""GIve summary for the data from transcript.txt:
    
    -Give me summary of data from the transcript.txt
    -Give data in multiple sections
    -The data should be simple and in a structured format
    -The data should be only from transcript.txt""",

    agent=summarizer,
    output_file="tasks_outputs/article_data.md",
)
