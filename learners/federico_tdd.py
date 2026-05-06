def is_zero(n):
    """Function to test if the argument is zero."""
    if n == 0:
        return True
    else:
        return False


assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)
