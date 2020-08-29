
# 1st Approach
class Base1:
    print('Base1')
    pass

class Base2:
    print('Base2')
    pass

class MultiDerived12(Base2, Base1):
    print('MultiDerived12')
    pass

MultiDerived12()

"""
Method Resolution Order (MRO).
"""""

print(MultiDerived12.__mro__)

# 2nd Approach
class Base3:
    print('Base3')
    pass

class Base4(Base3):
    print('Base4')
    pass

class MultiDerived34(Base4):
    print('MultiDerived34')
    pass

MultiDerived34()

"""
Every class in Python is derived from the object class. 
"""

# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))