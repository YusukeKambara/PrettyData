import unittest
from click.testing import CliRunner


class TestMain(unittest.TestCase):
    """Test class for testing the main module

    Arguments:
        unittest {[type]} -- [description]
    """

    @classmethod
    def setUpClass(cls):
        print("*" * 80 + "\nStart to test [main] module\n" + "*" * 80)

    def setUp(self):
        self.runner = CliRunner()