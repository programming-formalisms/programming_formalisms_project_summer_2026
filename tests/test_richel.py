"""Tests all code in src.learners.richel."""

import unittest

from weather.richel import get_name

class TestRichel(unittest.TestCase):

    """Class to test the code in src.learners.richel."""

    def test_get_name(self):
        """The function 'get_name' returns the correct name."""
        self.assertEqual(get_name(), "Richèl")
