#Exercise 3 JGC
def is_odd(n):
    """Returns True if n is odd, False otherwise. Accepts both integers, floats, and strings that can be converted to integers."""
    if not isinstance(n, int):
        try:
            n = int(n)
        except (ValueError, TypeError):
            raise ValueError("Input must be an integer or a string that can be converted to an integer.")
    if n % 2 == 0:
        return False
    else:
        return True
    
assert is_odd.__doc__ 
assert is_odd(1) == True
assert is_odd(2) == False
assert is_odd("1") == True
assert is_odd("2") == False
assert is_odd(1.0) == True
try:
    is_odd("This is not a number")
except ValueError:
    pass
assert is_odd(0) == False
assert is_odd(-1) == True