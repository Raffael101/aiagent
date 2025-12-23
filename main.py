import os
import argparse
from prompts import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from functions.call_funtion import call_function



def generate_content(client, messages, verbose, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt), 
        )
    
    if not response.usage_metadata:
        raise RuntimeError("Missing Usage Data")
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    tool_results = []
    for function_call_part in response.function_calls:
        result = call_function(function_call_part, verbose=verbose)
        if not  result.parts or not result.parts[0].function_response.response:
            raise Exception("Error: No response found? i think")
        tool_results.append(result.parts[0])
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
    has_function_calls = False
    try:
        messages.append(types.Content(role="user", parts=tool_results))
        for i in response.candidate:
            if not response.function_calls:
                return response.text
            final = generate_content(client, messages, args.verbose, args.prompt)    
            if final:
                print("Final response: ")
                print(response.text)
                break

  
    except Exception as e:
        print("Error:", e)

load_dotenv()
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
api_key = os.environ.get("GEMINI_API_KEY")
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, 
        schema_get_file_content,
        schema_run_python_file, 
        schema_write_file,
        ]
)
if api_key is None:
    raise RuntimeError("API key missing!")
client = genai.Client(api_key=api_key)
messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

generate_content(client, messages, args.verbose, args.prompt)

