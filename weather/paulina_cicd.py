"""Test function."""
def get_mean(list_of_numbers):
    """Compute the mean of list of numbers."""
    if not isinstance(list_of_numbers, list):
        mes = "Input must be a list."
        raise TypeError(mes)

    if len(list_of_numbers) == 0:
        mes = "Length of 'l' should be greater than 0."
        raise ValueError(mes)
    return sum(list_of_numbers) / len(list_of_numbers)

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

