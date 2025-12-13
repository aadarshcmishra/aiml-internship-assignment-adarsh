import requests

def call_ai_api(prompt):
    API_URL = "https://api.groq.com/openai/v1/chat/completions"
    API_KEY = "enter you api here"  # Replace with your gsk_ key

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",  # CORRECT MODEL
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]


prompt = "Explain the importance of AI in one sentence."
reply = call_ai_api(prompt)

with open("ai_output.txt", "w") as f:
    f.write(f"Prompt: {prompt}\n")
    f.write(f"Response: {reply}")

print("Saved to ai_output.txt")
