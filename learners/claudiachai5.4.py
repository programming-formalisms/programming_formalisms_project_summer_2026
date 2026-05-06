def is_prime(x):
    """ This function tests if the value is prime. """
    if x % 2 == 0:
        return False
    else:
        return True

    
assert is_prime.__doc__
assert is_prime(1)
#assert is_prime(2)
assert is_prime(3)
assert not is_prime(4) 