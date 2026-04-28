import unittest

from src.weather.analysis import do_analysis


class TestAnalysis(unittest.TestCase):

    def test_analysis_creates_two_files(self):
        do_analysis()
        import os.path
        self.assertTrue(os.path.isfile("figure.png"))
        self.assertTrue(os.path.isfile("statistics_results.txt"))
