from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["How does AI work?"])


print(response)