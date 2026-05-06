
def is_zero(x):
    """"
    Determine if the input is zero. Return True if zero, False if non-zero. Raises an exception if input is not a number.
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if (x == 0):
        return True
    else:
        return False

assert is_zero.__doc__
assert is_zero(0) == True
assert is_zero(1) == False
assert not is_zero(1)

has_thrown = False
try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown
