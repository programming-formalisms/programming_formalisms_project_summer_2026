def is_prime(x):
    """ This function tests if the value is prime. """
    try:
        x= int(x)
    except:
        return False
    if x % 2 == 0:
        print ('This is even')
        return False
    elif x/3> 1 and x % 3 == 0:
        print ('This can be divided by 3')
        return False
    else:
        return True

    
assert is_prime.__doc__
assert is_prime(1)
#assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert not is_prime(6)
assert not is_prime(9)
assert not is_prime("nonesense")
assert not is_prime(0.0)