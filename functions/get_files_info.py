import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    work = os.path.abspath(working_directory)
    tar = os.path.abspath(os.path.join(working_directory,directory))
    if not tar.startswith(work):
        return f'Result for {directory} directory:\n    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isdir(tar) == False:
        return f'Result for {directory} directory:\n    Error: "{directory}" is not a directory'
    elif directory == ".":
        dir = "Result for current directory: "
    elif directory == "..":
        dir = "Result for parent dircectory: "
    else:
        dir = f"Result for {directory} directory: "
    r_list = []
    for x in os.listdir(tar):
        item = tar +"/"+ x
        size = os.path.getsize(item)
        is_dir = os.path.isdir(item)
        r_string =  f" - {x}: file_size={size}, is_dir={is_dir}"
        r_list.append(r_string)
    j_string = "\n".join(r_list)
    return dir+"\n"+j_string