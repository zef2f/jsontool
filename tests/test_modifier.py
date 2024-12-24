import unittest
from jsontool.core.modifier import add_key_to_json
from jsontool.core.modifier import add_element_to_json_array

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

class TestAddElementToJsonArray(unittest.TestCase):

    def test_add_element_to_array(self):
        """Test adding an element to an existing JSON array."""
        json_obj = {"fruits": ["apple", "banana"]}
        updated_json = add_element_to_json_array(json_obj, "fruits", "cherry")
        self.assertIn("cherry", updated_json["fruits"])
        self.assertEqual(updated_json["fruits"], ["apple", "banana", "cherry"])

    def test_add_element_to_empty_array(self):
        """Test adding an element to an empty array."""
        json_obj = {"fruits": []}
        updated_json = add_element_to_json_array(json_obj, "fruits", "cherry")
        self.assertEqual(updated_json["fruits"], ["cherry"])

    def test_key_not_found(self):
        """Test that an error is raised if the key is not found in the JSON object."""
        json_obj = {"fruits": ["apple"]}
        with self.assertRaises(KeyError):
            add_element_to_json_array(json_obj, "vegetables", "carrot")

    def test_value_is_not_array(self):
        """Test that an error is raised if the value associated with the key is not a list."""
        json_obj = {"fruits": "apple"}
        with self.assertRaises(ValueError):
            add_element_to_json_array(json_obj, "fruits", "banana")

    def test_invalid_json_type(self):
        """Test that an error is raised if the JSON object is not a dictionary."""
        with self.assertRaises(TypeError):
            add_element_to_json_array([], "fruits", "cherry")

if __name__ == "__main__":
    unittest.main()
