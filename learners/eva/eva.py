def is_zero(num):
    """Check if input is zero. Return True if zero, False otherwise, Raises error if not a number.
    """
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be of type int or float")
    
    if num == 0:
        return True
    else:
        return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(10)

has_thrown = False
try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown