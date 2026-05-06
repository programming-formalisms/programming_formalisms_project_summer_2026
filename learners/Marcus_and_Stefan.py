def is_zero(x=None):
    """Determines if the input is one integer that is zero"""
    if x == None:
        raise TypeError("No value assinged")
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False


def is_even():
    """
    Checks if number is even.
    """

    pass

assert is_even.__doc__