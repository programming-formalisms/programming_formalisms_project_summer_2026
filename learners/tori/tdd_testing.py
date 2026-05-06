def is_zero(x):
    """Return True if the number is zero, False if the number is not zero"""
    
    if not isinstance(x, (int, float)):
        raise TypeError; "The valuex is not an int or float"
    if x == 0:
        return True
    else: 
        return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

has_thrown = False
try:   
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown


def is_even(x):
    """checks if number is even, returns True if yes, False if no"""
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    return x % 2 == 0

assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

has_thrown = False
try:   
    is_even(0.0)
except TypeError:
    has_thrown = True
assert has_thrown



def is_odd():
    """Checks if number is odd and returns True, otherwise False"""
    pass

assert is_odd.__doc__