"""
jsontool.core: Core functionality for JSON manipulation.

This module provides functions to read, write, modify, and navigate
JSON data.
"""

from .reader_writer import read_json_from_string, read_json_from_file, write_json_to_string, write_json_to_file
from .modifier import add_key_to_json, add_element_to_json_array
from .navigator import navigate_json
from .validator import validate_json

__all__ = [
    "read_json_from_string",
    "read_json_from_file",
    "write_json_to_string",
    "write_json_to_file",
    "add_key_to_json",
    "add_element_to_json_array",
    "navigate_json",
    "validate_json",
]
