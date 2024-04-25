import os
from dotenv import load_dotenv, find_dotenv
from dotenv import dotenv_values

# config = dotenv_values(".env")
# print(config.keys)

load_dotenv()

LANGCHAIN_TRACING_V2 = os.environ.get('LANGCHAIN_TRACING_V2')
LANGCHAIN_ENDPOINT = os.environ.get('LANGCHAIN_ENDPOINT')
LANGSMITH_API_KEY = os.environ.get('LANGSMITH_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
print({OPENAI_API_KEY})