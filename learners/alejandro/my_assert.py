#assert 1 == 2

def divide_by(numerator, denominator):
    assert isinstance(numerator, (float, int))
    assert isinstance(denominator, (float, int))
    assert type(numerator) == type(denominator)
    assert(denominator != 0.0)
    return (numerator / denominator)

print(divide_by(3, 4.5))
