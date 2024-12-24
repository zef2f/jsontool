import json

def read_json_from_string(json_string: str):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e.msg}")
