from pathlib import Path
import json

def read_json_from_string(json_string: str):
    """
    Parse a JSON string into a Python object.

    Args:
        json_string (str): The JSON string to be parsed.

    Returns:
        dict or list: The parsed JSON object.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains invalid JSON.
    """
    if not isinstance(json_string, str):
        raise TypeError("Input must be a string.")
    if not json_string.strip():
        raise ValueError("Input JSON string is empty.")
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e.msg}")

def read_json_from_file(file_path: str):
    """
    Read and parse JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The parsed JSON object.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are permission issues with the file.
        ValueError: If the file contains invalid JSON data.
    """
    file_path = Path(file_path)
    if not file_path.is_file():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    try:
        with file_path.open('r', encoding='utf-8') as file:
            return json.load(file)
    except PermissionError:
        raise PermissionError(f"Permission denied: '{file_path}'.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in the file '{file_path}': {e}")

def write_json_to_string(data, indent=None):
    """
    Serialize a Python object to a JSON string.

    Args:
        data (dict or list): The Python object to be serialized.
        indent (int, optional): Number of spaces for indentation in the output.
            Defaults to None (compact format).

    Returns:
        str: The JSON string representation of the data.

    Raises:
        TypeError: If the input data is not serializable to JSON.
        ValueError: If serialization fails.
    """
    if not isinstance(data, (dict, list)):
        raise TypeError("Input must be a dictionary or a list.")
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except TypeError as e:
        raise ValueError(f"Unable to serialize data to JSON: {e}")

def write_json_to_file(data, file_path: str, indent=None):
    """
    Write a Python object to a file in JSON format.

    Args:
        data (dict or list): The Python object to be written.
        file_path (str): The path to the file where JSON will be written.
        indent (int, optional): Number of spaces for indentation in the output.
            Defaults to None (compact format).

    Raises:
        TypeError: If the input data is not serializable to JSON.
        OSError: If there is an issue writing to the file.
    """
    if not isinstance(data, (dict, list)):
        raise TypeError("Input must be a dictionary or a list.")
    file_path = Path(file_path)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
    except TypeError as e:
        raise ValueError(f"Unable to serialize data to JSON: {e}")
    except OSError as e:
        raise OSError(f"Unable to write to file '{file_path}': {e}")
