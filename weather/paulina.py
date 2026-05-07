"""Compute the mean of list of numbers."""
def get_mean(list_of_numbers):
    """Compute the mean of list of numbers."""
    if not isinstance(list_of_numbers, list):
        raise TypeError("'l' must be a list.")
       
    if len(list_of_numbers) == 0:
        med = "lengths must not be 0"
        raise ValueError(mes)
    mean = sum(list_of_numbers) / len(list_of_numbers)
    return mean

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
