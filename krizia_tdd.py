def is_zero(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return x == 0


def is_even(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return x % 2 == 0

def is_odd(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return not is_even(x)

###test if zero####
assert is_zero(0) == True
assert is_zero(5) == False
assert is_zero(-3) == False

try:
    is_zero("0")
    assert False
except TypeError:
    pass

#### test for is_even####
assert is_even(2) ==True
assert is_even(10) ==True
assert is_even(3)  ==False
assert is_even(7) ==False

try:
    is_even("2")
    assert False
except TypeError:
    pass

##tests for is_odd###
assert is_odd(3) ==True
assert is_odd(7) == True
assert is_odd(2) == False
assert is_odd(10) == False

try:
    is_odd("3")
    assert False
except TypeError:
    pass

print("All tests passed!")
