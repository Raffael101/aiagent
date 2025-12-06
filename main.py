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
print(response.text)
def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
