def is_zero(x):
    """Determine if number is 0"""

    assert isinstance(x, (int, float))

    if x==0.0:
        return True
    return False



def is_even(x):
    """Determine if number is even"""

    assert is_even.__doc__
    assert isinstance(x, (int, float))

    if x % 2 == 0.0:
        return True
        



assert is_even(7)