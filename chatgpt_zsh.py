import openai
import os

api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

while True:
    prompt = input("You: ")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    message = response.choices[0].text.strip()
    print(f"ChatGPT: {message}")

