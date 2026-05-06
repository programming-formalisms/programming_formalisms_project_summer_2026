def get_mean(l):
    """Compute the mean of list of numbers"""
    if not isinstance(l, list):
        raise TypeError("'l' must be a list.")
    return True

assert get_mean.__doc__

has_thrown = False
try:
    assert get_mean(1)
except TypeError:
    has_thrown = True
assert has_thrown
    
assert isinstance([1], list)

assert get_mean([1]) == 1

