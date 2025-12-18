from google.genai import types
from functions.config import WORKING_DIR
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,    
    }
    f_args = dict(function_call_part.args)
    f_args["working_directory"]= WORKING_DIR
    if function_call_part.name in function_map:
        chosen_function = function_map[function_call_part.name]
        function_result = chosen_function(**f_args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": function_result},
        )],)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )],)