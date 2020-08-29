"""
Adding float in python PROBLEM

It turns out that the decimal fraction 0.1 will result in long binary fraction 0.1000000000000000055511151231257827021181583404541015625
and our computer only stores a finite number of it.

******* When to use Decimal instead of float? *******

# When we are making financial applications that need exact decimal representation.
# When we want to implement the notion of significant decimal places.
# When we want to control the level of precision required.

"""
print(1.1 + 2.2 == 3.3) # False
print(1.1 + 2.2) # 3.3000000000000003

from decimal import Decimal as D
print(D(0.1)) # 0.1000000000000000055511151231257827021181583404541015625
print(D('1.1') + D('2.2'))
print(D('1.2') * D('2.5'))
