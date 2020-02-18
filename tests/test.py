import unittest
import test_main
from tests.utils import test_utils
from tests.commands import test_analyze as test_commands_analyze
from tests.api import test_analyze as test_api_analyze

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(test_main.TestMain))
  suite.addTests(unittest.makeSuite(test_utils.TestUtils))
  suite.addTests(unittest.makeSuite(test_commands_analyze.TestCommandsAnalyze))
  suite.addTests(unittest.makeSuite(test_api_analyze.TestApiAnalyze))
  return suite