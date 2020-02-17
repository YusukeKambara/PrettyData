import os
import unittest
from pathlib import Path
from click.testing import CliRunner
from prettydata import main


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

    def test_main_no_command(self):
        """Testing for the main function with no argument
        """
        result = self.runner.invoke(main.cmd, [])
        assert result.exit_code == 0
        assert "First layer sub-command group" in result.output

    def test_main_non_defined_command(self):
        """Testing for the main function with non-defined command at first layer
        """
        result = self.runner.invoke(main.cmd, ["nondefined"])
        assert result.exit_code == 2
        assert "No such command" in result.output

    def test_main_analyze_command(self):
        """Testing for the main function with analyze comman
        """
        p = Path(os.getcwd() + "/tests/resources/for_analyze.csv")
        result = self.runner.invoke(main.analyze, [str(p)])
        assert result.exit_code == 0
        assert type(eval(result.output)) == dict