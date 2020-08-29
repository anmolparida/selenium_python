"""
Inheritance is a way of creating a new class for using  details of an existing class without modifying it.
The newly formed class is a derived class or child class.
The existing class is called a base class or parent class.
"""
class Planet():

    def __init__(self):
        print('Class Planet is ready')


# Parent Class
class Bird:

    def __init__(self):
        print('Class Bird is ready')

    def whoIsThis(self):
        print('Bird')

    def swim(self):
        print('Swim Faster')


# Child Class
class Penguin(Bird, Planet):

    def __init__(self):
        super().__init__()      # By default Super calls the first argument - parent class
        Planet.__init__(self)   # Explicitly calling in case of multiple inheritance
        print('Penguin is ready')

    def whoIsThis(self):
        print('Bird')

    def run(self):
        print('Run Faster')


peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()
