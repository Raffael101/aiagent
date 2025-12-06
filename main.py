import os
from dotenv import load_dotenv
from google import genai

content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API key missing!")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.5-flash", contents=content)
if response.usage_metadata() is None:
    raise RuntimeError("Missing Usage Data")
else:
    print(f"User prompt: {content}")
    print(f"Prompt tokens: {response.prompt_token_count}")
    print(f"Response tokens: {response.candidates_token_count}")
    print(response.text)
def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
