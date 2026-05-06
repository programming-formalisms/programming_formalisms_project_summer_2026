def is_even(x):
    if x == 0:
        print ('The number is 0')
        return False
    elif x % 2 ==0:
        return True
    else:
        return False


assert is_even(2)
assert not is_even(3) 
assert not is_even(0) 