

def check_corr(r):
    '''
    Check the value of a r values so it makes sense.
    '''
    if isinstance(r,float):
        if -1.0 <= r <= 1.0:
            return True
        else:
            raise ValueError("R needs to be between -1 and 1.")
    else:
        raise TypeError("R needs to be a float value.")
    
assert check_corr(1.0)
