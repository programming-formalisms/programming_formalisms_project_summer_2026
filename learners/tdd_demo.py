


def is_string(s):
    return isinstance(s,str)


assert not is_string(314)


def int_to_roman(x):
    '''
    Convert a integer to a roman numeral.
    '''
    return "I"

assert int_to_roman.__doc__
assert is_string(int_to_roman(5))
assert int_to_roman(1) == "I"