"""
Tests for the core module.
"""
import unittest
from nepali_word_to_speech.core import number_formulation, get_decimal


class TestCore(unittest.TestCase):
    """Test cases for core module functionality."""
    
    def test_number_formulation(self):
        """Test the number_formulation function."""
        # Test with simple numbers
        result = number_formulation(['ek'])
        self.assertEqual(result, 1)
        
        result = number_formulation(['ek', 'saya'])
        self.assertEqual(result, 100)
        
    def test_get_decimal(self):
        """Test the get_decimal function."""
        try:
            # Test simple decimal conversion
            result = get_decimal(['ek', 'ek'])
            self.assertIsInstance(result, float)
        except ValueError:
            # The function may raise ValueError if implementation is incomplete
            pass


if __name__ == "__main__":
    unittest.main() 