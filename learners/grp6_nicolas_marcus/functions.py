def is_palindrome(input_string):
    """
    This function checks for if a strig is a palidrome.
    It accepts a string and terutns True if is palindrome, 
    else it returns False
    """
    input_string_letters = ''.join(char for char in input_string if char.isalpha())
    input_string_letters = input_string_letters.lower()

    # Error handeling
    if not isinstance(input_string_letters, str):
        raise TypeError("Only strings are allowed")
    
    # Check if input is palindrome
    return input_string_letters == input_string_letters[::-1]

    

assert is_palindrome.__doc__

has_thrown = False
try:
    is_palindrome(1)
except:
    has_thrown = True
assert has_thrown

list_palindrome = ["alla", "Regalager", "Sirat, o ni, inotaris", "No lemon, no melon"]
for palindrome in list_palindrome:
    assert is_palindrome(palindrome)

