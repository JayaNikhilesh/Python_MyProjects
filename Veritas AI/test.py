import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("EXA_API")
print(f"API key is {api_key}")
