import unittest
import io
import pandas as pd
from commands import analyze as commands_analyze

class TestCommandsAnalyze(unittest.TestCase):
    """Test class for testing the analyze command module
    
    Arguments:
        unittest {[type]} -- [description]
    """

    @classmethod
    def setUpClass(cls):
        print("*" * 80 + "\nStart to test [commands.analyze] module\n" + "*" * 80)

    def test_analyze_normal_case(self):
        """Testing to be able to get the analyzed resutl 
        """
        test_data = """x,y,z
        12,22.45,777
        test,2019-09-17,0098
        """
        result = commands_analyze.analyze(io.StringIO(test_data))
        assert all(["most_common_type" in result[key] for key in result.keys()])
        assert all(["included_types" in result[key] for key in result.keys()])
        assert all(["loss_rate" in result[key] for key in result.keys()])
        assert all(["all_items" in result[key] for key in result.keys()])
        assert all(["unique_items" in result[key] for key in result.keys()])

    def test_analyze_irregular_case(self):
        """Testing to be able to get the analyzed resutl 
        """
        test_data = """,,"""
        assert commands_analyze.analyze(io.StringIO(test_data)) == {}