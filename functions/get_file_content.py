import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file path": types.Schema(
                type=types.Type.STRING,
                description="The path to  the file to read, relative to the working directory.",
            ),
        },
    ),
)




MAX_CHARS = 10000
def get_file_content(working_directory, file_path):
    work = os.path.abspath(working_directory)
    tar = os.path.abspath(os.path.join(working_directory,file_path))
    if not tar.startswith(work):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif os.path.isfile(tar) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
        
    else:
        with open(tar, "rb") as f:
            limit = f.read(MAX_CHARS)
            if len(limit) < MAX_CHARS:
                reached = False
            else:
                reached = True
        if reached == False:
            with open(tar, "r") as f:
                file_content_string = f.read(MAX_CHARS)
            return file_content_string
        elif reached == True:
            with open(tar, "r") as f:
                file_content_string = f.read(MAX_CHARS) +"\n"+'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
        else:
            return "Error: i dont know"
