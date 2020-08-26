"""
https://www.programiz.com/python-programming/object-oriented-programming
"""
# Parent Class
class Bird:

    def __init__(self):
        print('Bird is Ready')

    def whoIsThis(self):
        print('Bird')

    def swim(self):
        print('Swim Faster')


# Child Class - Inherits the Functions of the Parent Class
class Penguin(Bird):

    # Methods can be defined in any order but __init__ is executed first
    def __init__(self):
        # call super() function - allows us to run the __init__() method of the parent class inside the child class
        # [INTERVIEW] super().__init__() OR Bird.__init__(self)
        super().__init__()
        print("Penguin is ready")

    def whoIsThis(self):
        print('Penguin')
        super(Penguin, self).whoIsThis()

    def run(self):
        print('Run Faster')


# instantiate object
peggy = Penguin()
peggy.whoIsThis()
peggy.run()
peggy.swim()

