"""
jsontool.core: Core utilities for JSON manipulation.

This package provides functions for reading, writing, and transforming
JSON data, including support for file operations and string serialization.
"""

from .reader_writer import (
    read_json_from_string,
    read_json_from_file,
    write_json_to_string,
    write_json_to_file,
)

__all__ = [
    "read_json_from_string",
    "read_json_from_file",
    "write_json_to_string",
    "write_json_to_file",
]
