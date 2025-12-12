import os
import requests
import json

def call_ai_api(prompt):
    # NOTE: Replace with actual API Endpoint and Key
    API_URL = "https://api.openai.com/v1/chat/completions" 
    API_KEY = os.getenv("OPENAI_API_KEY") # Securely load key

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status() # Check for HTTP errors
        
        data = response.json()
        # Parsing the specific content from the response
        ai_reply = data['choices'][0]['message']['content']
        return ai_reply

    except requests.exceptions.RequestException as e:
        return f"API Error: {e}"

# --- Usage ---
prompt_text = "Explain the importance of AI in one sentence."
response_text = call_ai_api(prompt_text)

# Save to file
with open("ai_output.txt", "w") as f:
    f.write(f"Prompt: {prompt_text}\n")
    f.write(f"Response: {response_text}")

print("Output saved to ai_output.txt")
