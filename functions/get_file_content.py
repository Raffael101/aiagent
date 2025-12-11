import os
MAX_CHARS = 10000
def get_file_content(working_directory, file_path):
    work = os.path.abspath(working_directory)
    tar = os.path.abspath(os.path.join(working_directory,file_path))
    if not tar.startswith(work):
        print('Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return
    elif os.path.isfile(tar) == False:
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return
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
            print(file_content_string)
            return
        elif reached == True:
            with open(tar, "r") as f:
                file_content_string = f.read(MAX_CHARS) +"\n"+'[...File "{file_path}" truncated at 10000 characters]'
            print(file_content_string)
            return
        else:
            print("Error: i dont know")
            return
