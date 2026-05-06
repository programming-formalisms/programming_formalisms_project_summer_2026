def is_zero(x=None):
    """Determines if the input is one integer that is zero"""
    if x == None:
        raise TypeError("No value assinged")
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False


def is_even(number):
    """
    Checks if number is even.

    Returns True of value is even,
    else return False.

    """
    if not isinstance(number, int):
        raise TypeError("'Number' must be of type int")
    modulus_return = number % 2

    if modulus_return == 0:
        return True
    else:
        return False
    
    # Returns True if the input is even
    # Returns False if the input is not even
    # Gives an error when the input is not a number
assert is_even.__doc__
assert is_even(2)

has_thrown = False
try:
    is_even("nonsense")
except TypeError:
    has_thrown = True
assert has_thrown

