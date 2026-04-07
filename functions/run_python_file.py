import os
import subprocess
from pathlib import Path

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_file_path = os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist'
        if not Path(file_path_abs).suffix == ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_path_abs]

        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, timeout=30, text=True)
        output = ""

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        if result.stdout == "" and result.stderr == "":
            output += "No output produced\n"
        else:
            if result.stdout != "":
                output += f"STDOUT: {result.stdout}\n"
            if result.stderr != "":
                output += f"STDERR: {result.stderr}\n"

        return output
    
    except Exception as e:
        return f"Error running file: {e}"