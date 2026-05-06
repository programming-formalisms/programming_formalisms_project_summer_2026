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


def is_even():
    """checks if number is even, returns True if yes, False if no"""
    pass

assert is_even.__doc__