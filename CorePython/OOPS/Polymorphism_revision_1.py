"""
Polymorphism - same function name with different signatures

Polymorphism is an ability in OOP to use a common interface for multiple forms(data types)
Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
However we could use the same method to color any shape. This concept is called Polymorphism.
"""

class Parrot:

    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print('Parrot cant swim')


class Penguin:
    def fly(self):
        print('Penguin cant fly')

    def swim(self):
        print('Penguin can swim')



# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
blu.fly()
peggy.fly()

blu.swim()
peggy.swim()



