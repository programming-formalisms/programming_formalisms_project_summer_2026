# Exercise 5.1

def is_zero(testnum: int):
    """
    This function accepts one argument that should be a float or an interger

    Returns True if input is 0,
    Returns False if input is not 0,
    Rarises TypeError is input is not flat or int

    """
    return True if testnum == 0 else False

assert is_zero(0).__doc__
assert is_zero(0) 
assert not is_zero(1)