has_thrown = False

def is_odd(x):
    """This function checks if the value is odd."""
    global has_thrown

    try:
        x = int(x)
    except (TypeError, ValueError):
        has_thrown = True
        print("Invalid input")
        return False

    if x % 2 != 0:
        print("It is odd")
        return True
    print("It is even")
    return False


assert is_odd.__doc__

assert is_odd(1)
assert is_odd(3)
assert not is_odd(4)
assert is_odd(5)

is_odd("abc")
assert has_thrown
