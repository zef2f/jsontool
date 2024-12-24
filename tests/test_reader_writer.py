import unittest
from jsontool.core.reader_writer import read_json_from_string

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

if __name__ == '__main__':
    unittest.main()

