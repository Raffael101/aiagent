import os
import argparse
from prompts import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API key missing!")
client = genai.Client(api_key=api_key)
messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt), 
    )

if not response.usage_metadata:
    raise RuntimeError("Missing Usage Data")
elif args.verbose:
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
else:
    print(response.text)
def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
