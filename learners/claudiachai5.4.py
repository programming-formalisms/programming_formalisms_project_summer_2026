def is_prime(x):
    """ This function tests if the value is prime. """
    try:
        x= int(x)
    except:
        return False
    
    list_100=[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime=False

    if x == 0:
        return False
    else:
        for i in list_100:
            if x == i:
                prime=True
                return True 
            else:
                continue

            if prime == False:
                if x % i == 0:
                    print ('This can be divided by %s' %i)
                    return False 

#    else:
#        return True


 #   if x == 0:
 #       return False
 #   elif x % 2 == 0:
 #       print ('This is even')
 #       return False
    
 #   elif x/3> 1 and x % 3 == 0:
 #       print ('This can be divided by 3')
 #       return False
    
    

    
assert is_prime.__doc__
assert is_prime(1)
#assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert not is_prime(6)
assert not is_prime(9)
assert not is_prime("nonesense")
assert not is_prime(0.0)
