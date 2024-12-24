import unittest
from jsontool.core.modifier import add_key_to_json, add_element_to_json_array, remove_key_from_json, remove_element_from_json_array


class TestJsonModifier(unittest.TestCase):

    # Test cases for adding key to JSON
    def test_add_key_to_json_overwrite(self):
        json_data = {"key1": "value1"}
        result = add_key_to_json(json_data, "key2", "value2")
        self.assertEqual(result, {"key1": "value1", "key2": "value2"})

    def test_add_key_to_json_no_overwrite(self):
        json_data = {"key1": "value1"}
        with self.assertRaises(ValueError):
            add_key_to_json(json_data, "key1", "new_value", overwrite=False)

    def test_add_key_to_json_key_not_found(self):
        json_data = {"key1": "value1"}
        with self.assertRaises(KeyError):
            add_key_to_json(json_data, "key2", "value2", overwrite=False)

    # Test cases for adding element to JSON array
    def test_add_element_to_json_array_overwrite(self):
        json_obj = {"key1": ["item1", "item2"]}
        result = add_element_to_json_array(json_obj, "key1", "new_item", overwrite=True)
        self.assertEqual(result, {"key1": ["new_item"]})

    def test_add_element_to_json_array_no_overwrite(self):
        json_obj = {"key1": ["item1", "item2"]}
        result = add_element_to_json_array(json_obj, "key1", "new_item", overwrite=False)
        self.assertEqual(result, {"key1": ["item1", "item2", "new_item"]})

    def test_add_element_to_json_array_key_not_found(self):
        json_obj = {"key1": ["item1"]}
        with self.assertRaises(KeyError):
            add_element_to_json_array(json_obj, "key2", "new_item", overwrite=False)

    def test_add_element_to_json_array_invalid_type(self):
        json_obj = {"key1": "not_a_list"}
        with self.assertRaises(ValueError):
            add_element_to_json_array(json_obj, "key1", "new_item")

    # Test cases for removing key from JSON
    def test_remove_key_from_json(self):
        json_data = {"name": "Alice", "age": 30}
        result = remove_key_from_json(json_data, "age")
        self.assertEqual(result, {"name": "Alice"})

    def test_remove_key_from_json_key_not_found(self):
        json_data = {"name": "Alice", "age": 30}
        with self.assertRaises(KeyError):
            remove_key_from_json(json_data, "address")

    def test_remove_key_from_empty_json(self):
        json_obj = {}
        with self.assertRaises(KeyError):
            remove_key_from_json(json_obj, "key1")

    def test_remove_key_from_single_element_json(self):
        json_obj = {"key1": "value1"}
        result = remove_key_from_json(json_obj, "key1")
        self.assertEqual(result, {})

    # Test cases for removing element from JSON array
    def test_remove_element_from_json_array(self):
        json_obj = {"fruits": ["apple", "banana", "cherry"]}
        result = remove_element_from_json_array(json_obj, "fruits", "banana")
        self.assertEqual(result, {"fruits": ["apple", "cherry"]})

    def test_remove_element_not_found(self):
        json_obj = {"fruits": ["apple", "banana"]}
        with self.assertRaises(ValueError):
            remove_element_from_json_array(json_obj, "fruits", "grape")

    def test_key_not_found(self):
        json_obj = {"fruits": ["apple"]}
        with self.assertRaises(KeyError):
            remove_element_from_json_array(json_obj, "vegetables", "carrot")

    def test_value_is_not_array(self):
        json_obj = {"fruits": "apple"}
        with self.assertRaises(ValueError):
            remove_element_from_json_array(json_obj, "fruits", "banana")

    def test_empty_array(self):
        json_obj = {"fruits": []}
        with self.assertRaises(ValueError):
            remove_element_from_json_array(json_obj, "fruits", "banana")

    def test_delete_element_from_object(self):
        json_obj = {"fruits": {"apple": 1, "banana": 2}}
        with self.assertRaises(ValueError):
            remove_element_from_json_array(json_obj, "fruits", "apple")


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

    def test_overwrite_existing_key(self):
        """Test overwriting an existing key's array with a new element when `overwrite=True`."""
        json_obj = {"fruits": ["apple", "banana"]}
        updated_json = add_element_to_json_array(json_obj, "fruits", "cherry", overwrite=True)
        self.assertEqual(updated_json["fruits"], ["cherry"])

    def test_add_element_to_existing_key_without_overwrite(self):
        """Test adding an element to an existing key without overwriting."""
        json_obj = {"fruits": ["apple"]}
        updated_json = add_element_to_json_array(json_obj, "fruits", "banana", overwrite=False)
        self.assertEqual(updated_json["fruits"], ["apple", "banana"])


if __name__ == "__main__":
    unittest.main()
