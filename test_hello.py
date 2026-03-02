import unittest
from hello import greet


class TestGreet(unittest.TestCase):
    """Test cases for greet function"""
    
    def test_greet_with_name(self):
        """Test greeting with a simple name"""
        result = greet('World')
        self.assertEqual(result, 'Hello, World!')
    
    def test_greet_with_different_name(self):
        """Test greeting with a different name"""
        result = greet('Alice')
        self.assertEqual(result, 'Hello, Alice!')
    
    def test_greet_with_empty_string(self):
        """Test greeting with an empty string"""
        result = greet('')
        self.assertEqual(result, 'Hello, !')
    
    def test_greet_with_special_characters(self):
        """Test greeting with special characters"""
        result = greet('Alice-Bob')
        self.assertEqual(result, 'Hello, Alice-Bob!')
    
    def test_greet_with_numbers(self):
        """Test greeting with numbers in name"""
        result = greet('User123')
        self.assertEqual(result, 'Hello, User123!')


if __name__ == '__main__':
    unittest.main()
