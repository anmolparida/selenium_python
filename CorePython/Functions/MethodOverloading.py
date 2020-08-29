"""
Like other languages (for example method overloading in C++) do, python does not supports method overloading by default.
But there are different ways to achieve method overloading in Python.

The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.
"""

# Takes two argument and print their product
def product(a, b):
    p = a * b
    print(p)


# Second product method Takes three argument and print their product
def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)
