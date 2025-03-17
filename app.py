from flask import Flask, request, jsonify, send_from_directory
import requests
import os
import re
import markdown

app = Flask(__name__)

API_KEY = "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"  # Replace with your API key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def format_response(text):
  
    html = markdown.markdown(text)
    
   
    html = re.sub(r'(?<!\*)\*\s(.*?)(?=<br>|$)', r'<li>\1</li>', html)
    
   
    if '<li>' in html and '<ul>' not in html:
        html = re.sub(r'(<li>.*?</li>)+', r'<ul>\g<0></ul>', html)
    
    
    html = re.sub(r'(?m)^(\d+)\.\s+(.*?)$', r'<li>\2</li>', html)
    
  
    if '<li>' in html and '<ol>' not in html and re.search(r'(?m)^(\d+)\.\s+', text):
        html = re.sub(r'(<li>.*?</li>)+', r'<ol>\g<0></ol>', html)
    
    return html


def get_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
   
    enhanced_prompt = f"{prompt}\n\nPlease format your response with bullet points or numbered lists where appropriate, and ensure good readability."
    
    payload = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {
                "role": "user",
                "content": enhanced_prompt
            }
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        raw_response = response.json()["choices"][0]["message"]["content"]
        return format_response(raw_response)
    except requests.exceptions.RequestException as e:
        log_error(f"API Request Failed: {e}")
        return "Error: Unable to fetch response from AI."


def log_error(message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{message}\n")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat/<user_text>', methods=['GET'])
def chat(user_text):
    if not user_text:
        return jsonify({"response": "Error: No input provided."})
    
    response = get_ai_response(user_text)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)