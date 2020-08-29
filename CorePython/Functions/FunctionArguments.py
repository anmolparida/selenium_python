"""
# Python Keyword Arguments #

Python allows functions to be called using keyword arguments.
When we call functions in this way, the order (position) of the arguments can be changed.
Following calls to the above function are all valid and produce the same result.
"""

# Python Default Arguments

def greet(name, msg='Good Morning !'):
    """docstring inside greet function"""
    print("Hello", name , ".", msg)

greet('Rob')
greet('Richard', "Good Evening !")

# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce")

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")

# greet(name="Bruce","How do you do?") >> SyntaxError: positional argument follows keyword argument


"""
Python Arbitrary Arguments

Sometimes, we do not know in advance the number of arguments that will be passed into a function.
Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.
"""

def greet(*args):
    """This function greets all the person in the names tuple."""
    print(greet.__doc__)
    # names is a tuple with arguments
    for name in args:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")