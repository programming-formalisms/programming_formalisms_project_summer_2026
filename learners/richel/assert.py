
def is_zero(x):
    """Determine if the input is a zero.
    
    Returns True if the input is zero
    Returns False if the input is not zero
    Gives an error when the input is not a number
    """
    return(x == 0)


assert is_zero.__doc__
assert is_zero(0) == True
assert is_zero(1) == False
