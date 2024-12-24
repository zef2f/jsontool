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
