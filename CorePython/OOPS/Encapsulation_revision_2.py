"""
ENCAPSULATION
Using OOP in python, we can access to methods and variables.
This prevents data from direct modification which is called Encapsulation.
We denote private attributes using underscores as prefix  _variableName or __variableName
"""


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print('selling price', self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

#change the price
c.__maxprice = 1000 # it will not update
c.sell()

# using setter function
c.setMaxPrice(1000) # it will not update
c.sell()