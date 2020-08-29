class MyNewClass:
    """This is a docstring. I have created a new empty class"""
    print(__doc__)
    pass

# calling without creating an object of the class
MyNewClass

class Person:
    """This is a person class"""
    age = 10

    def greet(self):
        print('Hello')

p = Person()

# Output: 10
print('Person.age', Person.age)

# Output: <function Person.greet>
p.greet()

print(p.__doc__)

"""
Constructors in Python

Class functions that begin with double underscore __ are called special functions as they have special meaning.
Of one particular interest is the __init__() function. This special function gets called whenever a new object of that class is instantiated.

This type of function is also called constructors in Object Oriented Programming (OOP). We normally use it to initialize all the variables.

"""

print('\nComplexNumber')
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)