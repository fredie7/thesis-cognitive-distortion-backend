# Load environment variables and API key
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please provide the OPENAI_API_KEY")
else:
    print("API KEY FOUND")
