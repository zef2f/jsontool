import unittest
import json
import os
from jsontool.core.reader_writer import read_json_from_string
from jsontool.core.reader_writer import read_json_from_file
from jsontool.core.reader_writer import write_json_to_string


class TestReadJsonFromString(unittest.TestCase):
    
    def test_valid_json(self):
        json_string = '{"name": "Alice", "age": 25}'
        expected = {"name": "Alice", "age": 25}
        result = read_json_from_string(json_string)
        self.assertEqual(result, expected)
    
    def test_valid_empty_json(self):
        json_string = "{}"
        expected = {}
        result = read_json_from_string(json_string)
        self.assertEqual(result, expected)
    
    def test_invalid_json_missing_bracket(self):
        json_string = '{"name": "Alice", "age": 25'
        with self.assertRaises(ValueError) as context:
            read_json_from_string(json_string)
        self.assertTrue('Invalid JSON' in str(context.exception))
    
    def test_invalid_json_unexpected_char(self):
        json_string = '{"name": "Alice" age: 25}'
        with self.assertRaises(ValueError) as context:
            read_json_from_string(json_string)
        self.assertTrue('Invalid JSON' in str(context.exception))


class TestReadJsonFromFile(unittest.TestCase):

    def setUp(self):
        """Prepare test files"""
        self.valid_json = '{"name": "John", "age": 30, "city": "New York"}'
        self.invalid_json = '{"name": "John", "age": 30, "city": "New York"'
        self.test_file_valid = 'test_valid.json'
        self.test_file_invalid = 'test_invalid.json'
        self.test_file_nonexistent = 'test_nonexistent.json'
        
        # Create a valid JSON file
        with open(self.test_file_valid, 'w', encoding='utf-8') as f:
            f.write(self.valid_json)

        # Create an invalid JSON file
        with open(self.test_file_invalid, 'w', encoding='utf-8') as f:
            f.write(self.invalid_json)

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file_valid):
            os.remove(self.test_file_valid)
        if os.path.exists(self.test_file_invalid):
            os.remove(self.test_file_invalid)

    def test_read_valid_json(self):
        """Test reading a valid JSON file"""
        data = read_json_from_file(self.test_file_valid)
        self.assertEqual(data, {"name": "John", "age": 30, "city": "New York"})

    def test_read_invalid_json(self):
        """Test reading an invalid JSON file"""
        with self.assertRaises(ValueError):
            read_json_from_file(self.test_file_invalid)

    def test_file_not_found(self):
        """Test if a non-existent file raises FileNotFoundError"""
        with self.assertRaises(FileNotFoundError):
            read_json_from_file(self.test_file_nonexistent)

    def test_permission_error(self):
        """Test if permission issues are handled (skipped here but can be simulated with restricted file access)"""
        # You can test this with a file that has restricted permissions in real scenarios
        pass


class TestWriteJsonToString(unittest.TestCase):

    def test_write_dict(self):
        """Test converting a dictionary to JSON string"""
        data = {"name": "Alice", "age": 30, "city": "New York"}
        expected = '{"name": "Alice", "age": 30, "city": "New York"}'
        self.assertEqual(write_json_to_string(data), expected)

    def test_write_list(self):
        """Test converting a list to JSON string"""
        data = [1, 2, 3, 4]
        expected = "[1, 2, 3, 4]"
        self.assertEqual(write_json_to_string(data), expected)

    def test_pretty_print(self):
        """Test pretty-printed JSON string"""
        data = {"name": "Alice", "age": 30}
        expected = (
            '{\n'
            '  "name": "Alice",\n'
            '  "age": 30\n'
            '}'
        )
        self.assertEqual(write_json_to_string(data, indent=2), expected)

    def test_unicode_characters(self):
        """Test preserving unicode characters in JSON string"""
        data = {"message": "Привет, мир!"}
        expected = '{"message": "Привет, мир!"}'
        self.assertEqual(write_json_to_string(data), expected)

    def test_invalid_data(self):
        """Test handling non-serializable data"""
        data = {"name": "Alice", "func": lambda x: x}  # Lambdas are not serializable
        with self.assertRaises(ValueError):
            write_json_to_string(data)

if __name__ == '__main__':
    unittest.main()

