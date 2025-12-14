import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    work_dir = os.path.abspath(working_directory)
    tar_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not tar_dir.startswith(work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(tar_dir):
        return f'Error: File "{file_path}" not found.'
    elif not tar_dir.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    else:
        bash = ["python", file_path, *args]
        try:
            running = subprocess.run(
                bash,
                text=True, 
                capture_output=True,
                timeout=30, 
                cwd=work_dir
                )
        except Exception as e:
            return f"Error: executing Python file: {e}"
        out = running.stdout
        err = running.stderr
        if out == "" and err == "":
            return "No output produced"
        result = f"STDOUT:\n{out}\nSTDERR:\n{err}"
        if running.returncode != 0:
            return result +"\n"+ f"Process exited with code {running.returncode}"
        return result
        