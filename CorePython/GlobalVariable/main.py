from CorePython.GlobalVariable import config
from CorePython.GlobalVariable import update
# Prints the value that are updated in the update file
print(config.a)
print(config.b)

"""
Example 5: Using a Global Variable in Nested Function
"""


def foo():

    # global x # x in main: 25
    x = 20
    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main: ", x)
