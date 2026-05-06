def divide_by_3(numerator, denominator):
    assert isinstance(numerator, (float, int))
    assert isinstance(denominator, (float, int))
    assert type(numerator) == type(denominator)
    assert(denominator != 0.0)
    return (numerator/denominator)