import os

def get_files_info(working_directory, directory="."):
    work = os.path.abspath(working_directory)
    tar = os.path.abspath(os.path.join(working_directory,directory))
    phrase = f"Result for '{directory}' directory: "
    if not tar.startswith(work):
        print(phrase)
        print('Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    elif os.path.isdir(tar) == False:
        print(phrase)
        print(f'Error: "{directory}" is not a directory')
        return
    elif directory == ".":
        print("Result for current directory: ")
    elif directory == "..":
        print("Result for parent dircectory: ")
    else:
        print(phrase)


    for x in os.listdir(tar):
        item = tar +"/"+ x
        size = os.path.getsize(item)
        is_dir = os.path.isdir(item)
        print(f" - {x}: file_size={size}, is_dir={is_dir}")