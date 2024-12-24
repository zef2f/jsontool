from typing import Any, Dict

def add_key_to_json(json_data: Dict[str, Any], key: str, value: Any, overwrite: bool = True) -> Dict[str, Any]:
    """
    Adds a new key-value pair to the JSON object. If the key exists, either overwrite its value
    or raise an error depending on the 'overwrite' flag.

    Args:
        json_data (dict): The JSON object to modify.
        key (str): The key to add or update.
        value (Any): The value to associate with the key.
        overwrite (bool, optional): Whether to overwrite the existing value for the key. Defaults to True.

    Returns:
        dict: The modified JSON object.

    Raises:
        ValueError: If the key exists and overwrite is False.
    """
    if key in json_data and not overwrite:
        raise ValueError(f"Key '{key}' already exists. To overwrite, set 'overwrite=True'.")
    json_data[key] = value
    return json_data


def add_element_to_json_array(json_obj, key, element):
    """
    Adds an element to a JSON array at the specified key.

    Args:
        json_obj (dict): The JSON object containing the array.
        key (str): The key that holds the array.
        element (any): The element to add to the array.

    Returns:
        dict: The updated JSON object with the added element.

    Raises:
        TypeError: If the json_obj is not a dictionary.
        ValueError: If the value associated with the key is not an array.
    """
    if not isinstance(json_obj, dict):
        raise TypeError("Input must be a dictionary.")
    
    if key not in json_obj:
        raise KeyError(f"Key '{key}' not found in JSON object.")
    
    if not isinstance(json_obj[key], list):
        raise ValueError(f"The value associated with key '{key}' is not a list.")
    
    json_obj[key].append(element)
    return json_obj
