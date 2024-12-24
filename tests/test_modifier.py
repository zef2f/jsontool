import unittest
from jsontool.core.modifier import add_key_to_json

class TestJsonModifier(unittest.TestCase):

    def test_add_key_to_json(self):
        json_obj = {"name": "Alice", "age": 30}
        result = add_key_to_json(json_obj, "city", "New York")
        self.assertEqual(result, {"name": "Alice", "age": 30, "city": "New York"})

    def test_add_key_to_json_overwrite(self):
        json_obj = {"name": "Alice", "age": 30}
        result = add_key_to_json(json_obj, "age", 35, overwrite=True)
        self.assertEqual(result, {"name": "Alice", "age": 35})

    def test_add_key_to_json_no_overwrite(self):
        json_obj = {"name": "Alice", "age": 30}
        with self.assertRaises(ValueError):
            add_key_to_json(json_obj, "age", 35, overwrite=False)

if __name__ == "__main__":
    unittest.main()
