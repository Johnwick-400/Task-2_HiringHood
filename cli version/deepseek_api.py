import requests
import json

# API Configuration
API_KEY = "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"  # Replace with your API key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Function to send a prompt and retrieve the response
def get_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat:free",  # Use the desired model
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        log_error(f"API Request Failed: {e}")
        return None

# Function to log errors
def log_error(message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{message}\n")