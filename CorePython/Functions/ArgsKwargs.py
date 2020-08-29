"""
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)

"""
lst = [1, 2, 3]

def number(*args):
    print(args)
    for val in args:
        print(val*2)


lst = [1, 2, 3]
number(lst)


def adder(x,y,z):
    print("sum:",x+y+z)

adder(10,12,13)

def adder(x,y,z):
    print("sum:",x+y+z)

# adder(5,10,15,20,25) # TypeError: adder() takes 3 positional arguments but 5 were given

"""
*args : non-keyword arguments
"""

def adder(*num):
    total = 0
    for n in num:
        total = total + n
    print("total:", total)

adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

from functools import reduce
lst = [1, 2, 3, 5, 6]
output = reduce(lambda x, y : x + y, lst )
print(output)

"""
**kwargs : keyword arguments
"""

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)