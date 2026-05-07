"""Test function."""
def get_mean(l):
    """Compute the mean of list of numbers."""
    if not isinstance(l, list):
        raise TypeError("")
    
    if len(l) == 0:
        raise ValueError("")
    return sum(l) / len(l)

assert get_mean.__doc__

has_thrown = False
try:
    assert get_mean(1)
except TypeError:
    has_thrown = True
assert has_thrown
 
assert isinstance([1], list)

assert get_mean([1]) == 1

has_thrown = False
try:
    assert get_mean([])
except ValueError:
    has_thrown = True
assert has_thrown

