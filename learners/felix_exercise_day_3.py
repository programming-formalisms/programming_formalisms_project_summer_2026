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

def is_even(x):
    """The function tests if a given number is even."""
    if not isinstance(x, int):
        raise TypeError("a must be of type Integer")
    if (x % 2 == 0):
        return True
    else:
        return False

assert is_even.__doc__
assert is_even(2) == True
assert is_even(1) == False

has_returned = False
try: 
    is_even("nonsense")
except: 
    has_returned = True
assert has_returned