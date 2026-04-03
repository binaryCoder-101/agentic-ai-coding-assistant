import os

def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_file_path = os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs
        parent_dir = os.path.dirname(file_path_abs)
        os.makedirs(parent_dir, exist_ok=True)
        
        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        with open(file_path_abs, 'w', encoding='utf-8') as f:
            f = content
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error writing to file: {e}"
