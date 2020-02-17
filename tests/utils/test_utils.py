from os.path import basename
import unittest
from datetime import datetime
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
        # Cast to [datetime]
        assert type(utils.safe_cast("02/14/2020", datetime)) == datetime
        assert type(utils.safe_cast("2020/02/14", datetime)) == datetime
        assert type(utils.safe_cast("2020/02/14 14:00:30", datetime)) == datetime
        # Cast to [list]
        assert type(utils.safe_cast("[1, '2', 'test', 0.45]", list)) == list
        # Cast to [tuple]
        assert type(utils.safe_cast("(1, '2', 'test', 0.45)", tuple)) == tuple
        # Cast to [str]
        assert type(utils.safe_cast("999", str)) == str
        assert type(utils.safe_cast(123, str)) == str
        # Cast None value to None
        assert type(utils.safe_cast(None, int)) == type(None)
        assert type(utils.safe_cast(None, float)) == type(None)
        assert type(utils.safe_cast(None, datetime)) == type(None)
        assert type(utils.safe_cast(None, list)) == type(None)
        assert type(utils.safe_cast(None, tuple)) == type(None)

    def test_safe_cast_irregular_case(self):
        """Testing to be able to get None value or not if can not be cast the value
        """
        # Cast to [int]
        assert utils.safe_cast("test", int) == None
        # Cast to [float]
        assert utils.safe_cast("test", float) == None
        # Cast to [datetime]
        assert utils.safe_cast("02/33/2020", datetime) == None
        assert utils.safe_cast("test", datetime) == None
        # Cast to [list]
        assert utils.safe_cast("1 '2' 'test' 0.45", list) == None
        # Cast to [tuple]
        assert utils.safe_cast("1 '2' 'test' 0.45", tuple) == None

    def test_judge_type_normal_case(self):
        """Testing to be able to judge of standard types or not
        """
        # Try to judge with tuple string
        assert utils.judge_type("(1, '2', 3, 'test')")== tuple
        # Try to judge with list string
        assert utils.judge_type("[1, '2', 3, 'test']") == list
        # Try to judge with datetime string
        assert utils.judge_type("02/14/2020") == datetime
        assert utils.judge_type("2020/02/14 14:00:30") == datetime
        # Try to judge with int string
        assert utils.judge_type("123") == int
        # Try to judge with float string
        assert utils.judge_type("123.456") == float
        # Try to judge with str string
        assert utils.judge_type("test string") == str

    def test_judge_type_irregular_case(self):
        """Testing to be not able to judge of standard types or not
        """
        # TODO I cannot imagine the way of checking this case. So I'll create later