import os

def get_files_info(working_directory, directory="."):
    work = os.path.abspath(working_directory)
    tar = os.path.abspath(os.path.join(working_directory,directory))
    if not tar.startswith(work):
        return f'Result for {directory} directory:\nError: Cannot list "{directory}" as it is outside the permitted working directory'
    elif os.path.isdir(tar) == False:
        return f'Result for {directory} directory:\nError: "{directory}" is not a directory'
    elif directory == ".":
        dir = "Result for current directory: "
    elif directory == "..":
        dir = "Result for parent dircectory: "
    else:
        dir = f"Result for {directory} directory: "
    for x in os.listdir(tar):
        item = tar +"/"+ x
        size = os.path.getsize(item)
        is_dir = os.path.isdir(item)
        return f"{dir} - {x}: file_size={size}, is_dir={is_dir}"