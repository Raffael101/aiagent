import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes/creates file and contents in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write/create, relative to the working directory.",
            ),
              "content": types.Schema(
                type=types.Type.STRING,
                description="The contents of the file to write/create."
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    work_dir = os.path.abspath(working_directory)
    tar_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not tar_dir.startswith(work_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif os.path.exists(tar_dir) == False and os.path.exists(os.path.dirname(tar_dir)) == False:
        with open(tar_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    elif os.path.exists(tar_dir) == False:
        directory = os.path.dirname(tar_dir)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(tar_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    elif os.path.exists(tar_dir):
        with open(tar_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    else:
        raise Exception("Error: something wrong with the if statement")