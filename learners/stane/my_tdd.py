# Exercise 5.1

def is_zero(testnum: int) -> bool:
    """
    This function accepts one argument that should be a float or an interger

    Returns True if input is 0,
    Returns False if input is not 0,
    Rarises TypeError is input is not float or int

    """
    if not isinstance(testnum, (float,int)):
        raise TypeError("Input must be of type int or float")
    return True if testnum == 0 else False

assert is_zero(0).__doc__
assert is_zero(0) 
assert not is_zero(1)
has_thrown = False
try:
    is_zero('somestring')
except:
    has_thrown = True
assert has_thrown

# Exercise 5.2

def is_even(testnum: int) -> bool:
    """
    This function accepts one argument that should be a float or an interger

    Returns True if input is even number,
    Returns False if input is odd number or zero,
    Rarises TypeError is input is not float or int

    """
    return True

assert is_even(0).__doc__
assert is_even(2)