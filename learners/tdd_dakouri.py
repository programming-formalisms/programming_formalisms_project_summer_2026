print()

def is_even(n):
    """Determines if input is an even integer"""
    return n % 2 == 0

assert is_even.__doc__
assert is_even(2)
assert not is_even(3)

print()