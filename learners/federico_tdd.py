def is_zero(n):
    """Test if the argument is zero."""
    if not isinstance(n, int):
        raise TypeError("'n' is not an integer")
    if n == 0:
        return True
    else:
        return False


assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

is_thrown = False
try:
    is_zero("zero")
except:
    is_thrown = True

assert is_thrown


def is_prime(n, d=2):
    """Check if the argument is a prime number."""
    if n < 2:
        return False
    elif n == d:
        return True
    elif n % d == 0:
        return False
    else:
        return is_prime(n, d + 1)


assert is_prime.__doc__
assert not is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
