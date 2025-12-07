import os
import argparse
from dotenv import load_dotenv
from google import genai


load_dotenv()
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="User prompt")
args = parser.parse_args()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API key missing!")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.5-flash", contents=args.prompt)
if not response.usage_metadata:
    raise RuntimeError("Missing Usage Data")
else:
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
