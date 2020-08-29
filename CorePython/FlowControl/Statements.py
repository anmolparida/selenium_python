"""
-   In Python, we don't actually assign values to the variables. Instead, Python gives the reference of the object(value) to the variable.

-   Instructions that executed are called statements

-   Python is a type-inferred language, so you don't have to explicitly define the variable type.
    It automatically knows that apple.com is a string and declares the website variable as a string.

**********************************************
Naming Convention for Variables and constants
**********************************************

snake_case
MACRO_CASE
camelCase
CapWords
CONSTANT
Never use special symbols like !, @, #, $, %, etc.
Don't start a variable name with a digit.

"""

# multi line statements
a = 1 + \
    2 + \
    3
print(a)

b = (1 +
     2 +
     3)
print(b)

a, b,  c = 1, 2, 3
print(a,b,c)

a = 1; b = 2; c = 3
print(a,b,c)

def cube(n):
    """DocStrings in Python - used for explaining the function"""
    print(cube.__doc__)
    print(pow(n,3))

cube(7)


a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

x = y = z = "same"

print (x)
print (y)
print (z)

from CorePython.FlowControl import constant
print("\nfrom CorePython.FlowControl import constant")
print(constant.PI)
print(constant.GRAVITY)