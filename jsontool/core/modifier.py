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


def add_element_to_json_array(json_obj, key, element, overwrite=False):
    """
    Adds an element to a JSON array at the specified key. If the key already exists,
    it either raises an error or overwrites the existing value based on the `overwrite` parameter.

    Args:
        json_obj (dict): The JSON object containing the array.
        key (str): The key that holds the array.
        element (any): The element to add to the array.
        overwrite (bool): Whether to overwrite the existing array if the key already exists.

    Returns:
        dict: The updated JSON object with the added element.

    Raises:
        TypeError: If the json_obj is not a dictionary.
        ValueError: If the value associated with the key is not a list.
        KeyError: If the key does not exist and `overwrite` is False.
    """
    if not isinstance(json_obj, dict):
        raise TypeError("Input must be a dictionary.")

    if key not in json_obj:
        if overwrite:
            # If `overwrite` is True, create a new array with the element
            json_obj[key] = [element]
        else:
            # Raise an error if the key is not found and overwrite is False
            raise KeyError(f"Key '{key}' not found in the JSON object.")
    else:
        if not isinstance(json_obj[key], list):
            raise ValueError(f"The value associated with key '{key}' is not a list.")

        if overwrite:
            # Overwrite the existing array with the new element
            json_obj[key] = [element]
        else:
            # Add the element to the existing array
            json_obj[key].append(element)

    return json_obj
