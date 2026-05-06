# Create is_zero function

def is_zero(a):
    """The function tests is a given number is zero."""
    if not isinstance(a, int):
        raise TypeError("a must be of type Integer")
    if (a == 0):
        return True
    else:
        return False

assert is_zero.__doc__
assert is_zero(0) == True
assert is_zero(1) == False

has_thrown = False
try: 
    is_zero("nonsense")
except: 
    has_thrown = True
assert has_thrown

# Create is_even function

def is_even(a):
    """The function tests if a given number is even."""
    if (a % 2 == 0):
        return True
    else:
        return False

assert is_even.__doc__
assert is_even(2) == True