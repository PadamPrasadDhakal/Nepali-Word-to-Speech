#!/usr/bin/env python
"""
Run all tests for nepali_word_to_speech.
"""
import unittest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('nepali_word_to_speech/tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite) 