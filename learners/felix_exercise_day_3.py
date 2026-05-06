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

# Create the is_odd function, based on the is_even function.

def is_odd(y):
    """The function returns True if the given number is odd, else False."""
    if not isinstance(y, int):
        raise TypeError("y must be of type Integer")
    if is_even(y) == True:
        return False
    else:
        return True

assert is_odd.__doc__
assert is_odd(1) == True
assert is_odd(2) == False

has_given = False
try: 
    is_odd("nonsense")
except: 
    has_given = True
assert has_given

# Create the is_prime function

