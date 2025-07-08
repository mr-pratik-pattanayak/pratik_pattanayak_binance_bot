from dotenv import load_dotenv
import os

# Explicitly load the .env file from your project root directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


