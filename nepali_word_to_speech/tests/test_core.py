"""
Tests for the core module.
"""
import unittest
from nepali_word_to_speech.core import speak, text_to_audio_file, example_function, add_numbers


class TestCore(unittest.TestCase):
    """Test cases for core module functionality."""
    
    def test_speak(self):
        """Test the speak function returns True."""
        result = speak("नमस्ते")
        self.assertTrue(result)
    
    def test_text_to_audio_file(self):
        """Test the text_to_audio_file function returns True."""
        result = text_to_audio_file("नमस्ते", "output.mp3")
        self.assertTrue(result)
    
    def test_example_function(self):
        """Test the example_function returns the expected string."""
        result = example_function()
        self.assertEqual(result, "Welcome to yourpackage!")
    
    def test_add_numbers(self):
        """Test the add_numbers function correctly adds two numbers."""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main() 