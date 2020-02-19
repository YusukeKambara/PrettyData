import dateutil.parser
from datetime import datetime

def safe_cast(val, cast_type, default_val=None):
    """Try to cast the argument value. If it can not be cast, return the default value.
    
    Arguments:
        val {any} -- Value to try to cast
        cast_type {type} -- Type to cast
    
    Keyword Arguments:
        default_val {same type of 'val'} -- Value to be not able to cast with the argument (default: {None})
    
    Returns:
        [cast_type] -- Casted value
    """
    try:
        return cast_type(val)
    except:
        return default_val

def judge_type(val):
    return type(
        safe_cast(val, int, safe_cast(val, float, safe_cast(val, str)))
    )
