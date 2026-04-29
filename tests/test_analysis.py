"""The analysis must work as expected."""
import os.path
import unittest

from src.weather.analysis import do_analysis


class TestAnalysis(unittest.TestCase):

    """The analysis must work as expected."""

    def test_analysis_creates_two_files(self):
        """An analysis must create a figure and statistics results file."""
        do_analysis()
        self.assertTrue(os.path.isfile("figure.png"))
        self.assertTrue(os.path.isfile("statistics_results.txt"))
