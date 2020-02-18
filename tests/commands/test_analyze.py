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


