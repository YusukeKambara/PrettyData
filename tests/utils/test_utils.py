from os.path import basename
import unittest
from prettydata.utils import utils

class TestUtils(unittest.TestCase):
    """Test class for testing the utils module
    
    Arguments:
        unittest {[type]} -- [description]
    """

    @classmethod
    def setUpClass(cls):
        print("*" * 80 + "\nStart to test [utils] module\n" + "*" * 80)

    def test_safe_cast_normal_case(self):
        """Testing to be able to cast the value with argument's type
        """
        # Cast to [int]
        assert type(utils.safe_cast("123", int)) == int
        assert type(utils.safe_cast("-123", int)) == int
        # Cast to [float]
        assert type(utils.safe_cast("123.45", float)) == float
        assert type(utils.safe_cast("-123.00", float)) == float
        # Cast to [str]
        assert type(utils.safe_cast("999", str)) == str
        assert type(utils.safe_cast(123, str)) == str

    def test_safe_cast_irregular_case(self):
        """Testing to be able to get None value or not if can not be cast the value
        """
        # Cast to [int]
        assert utils.safe_cast("test", int) == None
        # Cast to [float]
        assert utils.safe_cast("test", float) == None