import unittest
import io
import pandas as pd
from commands import analyze as command_analyze

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
        test_data = io.StringIO()
        test_data.write("x,y,z\n")
        test_data.write("12,22.45,45\n")
        test_data.write("'test',2019-09-17,'0098'\n")
        test_data.seek(0)
        df = pd.read_csv(test_data)
        result = command_analyze.analyze(df)
        assert "most_common_type" in result.columns
        assert "included_types" in result.columns
        assert "loss_rate" in result.columns
        assert "all_items" in result.columns
        assert "unique_items" in result.columns


