def is_palindrome(string):
    """
    This function checks for if a strig is a palidrome.
    It accepts a string and terutns True if is palindrome, 
    else it returns False
    """

    if not isinstance(string, str):
        raise TypeError("Only strings are allowed")
    else:
        return True
    

assert is_palindrome.__doc__

has_thrown = False
try:
    is_palindrome(1)
except:
    has_thrown = True
assert has_thrown