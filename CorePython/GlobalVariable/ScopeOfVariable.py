"""
# Global Variables

# Local Variables

# Nonlocal Variables

    # Nonlocal variables are used in nested functions whose local scope is not defined.
    # This means that the variable can be neither in the local nor the global scope.
    # Let's see an example of how a global variable is created in Python.

We use nonlocal keywords to create nonlocal variables
"""

def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner', x)
    inner()
    print('outer', x)

outer()

# Global Variable #

c = 1 # global variable
def add():
    global c
    c = c + 2
    print(c)
add()
print(c)



