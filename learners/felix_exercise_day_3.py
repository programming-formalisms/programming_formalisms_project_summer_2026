# Create is_zero function

def is_zero(a):
    """The function tests is a given number is zero."""
    if (a == 0):
        return True
    else:
        return False

assert is_zero.__doc__
assert is_zero(0) == True
assert is_zero(1) == False