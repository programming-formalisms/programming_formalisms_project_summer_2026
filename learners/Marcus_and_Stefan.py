def is_zero(x=None):
    """Determines if the input is one integer that is zero"""
    if x == None:
        raise TypeError("No value assinged")
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False

assert is_zero()


# Returns True if the input is even
# Returns False if the input is not even
# Gives an error when the input is not a number