import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_file_path = os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs
        
        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        parent_dir = os.path.dirname(file_path_abs)
        os.makedirs(parent_dir, exist_ok=True)
        with open(file_path_abs, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error writing to file: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file that needs to be modified",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that needs to be written to the file",
            ),
        },
    ),
)