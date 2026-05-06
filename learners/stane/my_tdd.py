# Helper funtions
def is_number(testnum):
    if not isinstance(testnum, (float,int)):
        raise TypeError("Input must be of type int or float")

def is_perfect_square_float(n: int) -> bool:
    import math
    if n < 0:
        return False
    return math.sqrt(n).is_integer()

# Exercise 5.1
def is_zero(testnum: int) -> bool:
    """
    This function accepts one argument that should be a float or an interger

    Returns True if input is 0,
    Returns False if input is not 0,
    Rarises TypeError is input is not float or int

    """
    is_number(testnum)
    return True if testnum == 0 else False

assert is_zero(0).__doc__
assert is_zero(0) 
assert not is_zero(1)
has_thrown = False
try:
    is_zero('somestring')
except:
    has_thrown = True
assert has_thrown

# Exercise 5.2
def is_even(testnum: int) -> bool:
    """
    This function accepts one argument that should be a float or an interger

    Returns True if input is even number,
    Returns False if input is odd number or zero,
    Rarises TypeError is input is not float or int

    """
    is_number(testnum)
    if testnum == 0 or testnum%2 != 0:
        return False
    elif testnum%2 == 0:
        return True
    else:
        raise ValueError("The input is neither even nor odd number")

assert is_even(0).__doc__
assert is_even(2)
assert not is_even(5)
assert not is_even(0)
has_thrown = False
try:
    is_even('somestring')
except:
    has_thrown = True
assert has_thrown

# Exercise 5.3
def is_odd(testnum: int) -> bool:
    """
    This function accepts one argument that should be a float or an interger

    Returns True if input is odd number,
    Returns False if input is even number or zero,
    Rarises TypeError is input is not float or int

    """
    is_number(testnum)
    if testnum == 0 or testnum%2 == 0:
        return False
    elif testnum%2 != 0:
        return True
    else:
        raise ValueError("The input is neither even nor odd number")

assert is_odd(0).__doc__
assert is_odd(5)
assert not is_odd(2)
assert not is_even(0)
has_thrown = False
try:
    is_even('somestring')
except:
    has_thrown = True
assert has_thrown

# Exercise 5.4
def is_prime(n:int):
    import math
    """
    This function accepts one argument that should be an interger

    Returns True if input is a prime,
    Returns False if input is not a prime,
    Raises TypeError is input is not an int

    """
    if not isinstance(n, int):
        raise TypeError("The input is not an int")

    if n <= 1:
        return False
    elif n == 2: 
        return True
    elif is_even(n):
        return False
    if is_perfect_square_float(n):
        return False
    i = 3
    while i < n/2:
        if n%i == 0:
            return False
        i+=1
    return True


assert is_prime(0).__doc__
assert not is_prime(0)
assert not is_prime(1)
assert is_prime(2)
assert not is_prime(4)
assert not is_prime(9)
assert is_prime(17)
assert not is_prime(33)
assert not is_prime(68467)
assert is_prime(68473)