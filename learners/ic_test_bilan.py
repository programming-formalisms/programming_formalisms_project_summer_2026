#How to fix 'Check code style'?
learners/probability.py:13:5: RET505 [*] Unnecessary `else` after `return` statement
   |
11 |     if (x>0.0) & (x<1.0):
12 |         return True
13 |     else:
   |     ^^^^ RET505
14 |         return False

if (x>0.0) & (x<1.0):
    return True
else:
    return False

if (x>0.0) & (x<1.0):
    return True
return False

return x > 0.0 && x < 1.0