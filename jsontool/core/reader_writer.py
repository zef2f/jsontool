import json
import os

def read_json_from_string(json_string: str):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e.msg}")

def read_json_from_file(file_path):
    """
    Reads JSON data from a file and parses it into a Python object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The parsed JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there are permission issues with the file.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except PermissionError:
        raise PermissionError(f"Permission denied while accessing the file '{file_path}'.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in the file '{file_path}': {e}")

