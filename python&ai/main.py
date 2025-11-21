import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = os.getenv("API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {"role": "user", "content": "Hello GPT, I am writing from Python for the first time!"}
    ],
    "max_tokens": 100,
    "temperature": 0
}

response = requests.post(api_endpoint, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print("failed", response.status_code, response.text)
