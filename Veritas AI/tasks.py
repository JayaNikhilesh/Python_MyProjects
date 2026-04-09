import os

from crewai import Task
from openpyxl.styles.builtins import output

from agents import researcher, writer, editor

os.makedirs("tasks_outputs", exist_ok=True)

#Task1 Collect the data from {query} and collect the top trending keywords and articles on that {topic}
researcher_task=Task(
    description="""Look for top trending keywords and articles on {topic} using EXASearchTool
    
    your data should contain:
    1.TOp trending keyword or article from that {topic}
    2.Should be officially confirmed
    3.Should not give data from unofficial sources without the user permission or until he says
    4.Should give detailed information
    5.Should not show my API keys or other sensitive information in verbose also
    6.The articles should have more content about the {topic}
    7.The articles should have data in them
    8.Get the latest keywords or articles on the {topic}
    9.Only get the old data if the user specify
    
    Focus on finding the keywords and {topic} from EXASearchTool""",
    expected_output="""GIve me the list of keywords and articles from the {topic}:
    
    -Give the list of Keywords and articles from the {topic}
    -The list should be very simple
    -The data should be only top searches or keywords that are used repeatedly
    -The data should have links to that specific article
    -Hide the sensitive information like API_KEYS in the data or dont add the details in data
    -The articles should have information in them, there should not be errors when opening the articles""",

    agent=researcher,
    output_file="tasks_outputs/article_data.md",
)

# Task2 Collect the data and write the blogs based on the data
writer_task = Task(
    description="""Should write a blog from the data on that that {topic}

    your data should contain:
    1.The blog should contain the keywords or articles from that {topic}
    2.The blog should not contain any unofficial information or illegal content
    3.The blog should be read by all the people and they should not get bored of the content
    4.The blog should make the users to read other blogs because of the good and useful content
    5.Hide the sensitive information like API_KEYS in data and in my verbose
    6.The data should be accessible
    7.There should not be any errors in the articles
    8.Write the blogs on only latest information on the {topic} except the user specify

    Focus on creating the blog with the top trending keywords or top articles from the {topic}""",
    expected_output="""GIve me the list of keywords and articles from the {topic}:
    
    -The blog is legal and contain only official data
    -The blog should be easy to understand
    -The blog is related to the {topic} we search
    -The blog should be exciting or make the user to check for other blogs 
    -The blogs can be used for knowledge purpose
    -The blogs should be accessible
    -the blogs should contain data about the {topic} but not errors""",
    agent=writer,
    context=[researcher_task],
    output_file="tasks_outputs/blogs.md",
)

# Task3 Collect the data and make the blogs more keyword density and scoring readability
editor_task = Task(
    description="""Should edit the blogs given by into more detailed and scoring readability

    your data should contain:
    1.The edited blogs should be contain legal and officially confirmed
    2.The blog should be easy to understand
    3.The blogs should mainly contain keywords or articles from the {topic}
    4.The edited blogs should have meta data descriptions
    5.The blogs should be more data with less waste data 
    6.Hide the sensitive information like API_KEYS and other information in data and o9n verbose
    7.The links should be opened and should contain information about the {topic}
    8.The links opened should not contain errors or data not found on the {topic}
    9.The blogs should be created on the latest news on that {topic}

    Focus on updating and refining the data and by increasing the keyword density, adding meta data""",
    expected_output="""GIve me the best blog from that content with more keyword density, scoring readability:

    -The blog has official content.
    -The blog has meta data.
    -The blog should have more keywords and articles on the {topic} i gave
    -Links to the articles it searched online as proofs
    -The blogs have good titles
    -The blogs should have data with high keyword density
    -Should add meta data according to the {topic}
    -The blog should have scoring readability
    -The links should be opened and have data according to the {topic}""",
    agent=editor,
    context=[researcher_task, writer_task],
    output_file="tasks_outputs/final_blog.md",
)