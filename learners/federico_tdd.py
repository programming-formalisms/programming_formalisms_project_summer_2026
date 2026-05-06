def is_zero(n):
    """Function to test if the argument is zero."""
    if not isinstance(n, int):
        raise TypeError("'n' is not an integer")
    if n == 0:
        return True
    else:
        return False


assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

is_thrown = False
try:
    is_zero("zero")
except:
    is_thrown = True
assert is_thrown
