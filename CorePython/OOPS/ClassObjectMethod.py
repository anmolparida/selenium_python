"""

https://www.programiz.com/python-programming/object-oriented-programming

Object has 2 characteristics : attribute and behaviour
Parrot attributes: name, age, color
Parrot behaviour : singing and dancing

class has all the attributes of the parrot

# from class we construct instances
# Instance is a specific object created from a specific class
# obj is an instance of the class
# when a class is defined only the description of the class is defines, no memory is allocated

# empty class
class Peacock:
    pass

"""

# PARENT CLASS
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute #
    # the attributes are defines inside the __init__ (not a constructor)
    # constructor is run as sson as the object is creted
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    # instant method #
    # [INTERVIEW] self is a reference to the current instance of the class

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    #  usually the first parameter of the method is named 'self' although it can be renamed, in this case 'self_renamed'
    def dance(self_renamed):
        return "{} is now dancing".format(self_renamed.name)


# instantiate the parrot class - objects
blu = Parrot("Blu", 10, 'override_bird')
woo = Parrot("Woo", 15, 'override_bird')

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

# access the instance attributes
print("{0} is a {2}, {0} is {1} years old".format(blu.name, blu.age, blu.species))
print("{0} is a {2}, {0} is {1} years old".format(blu.name, blu.age, blu.__class__.species))

# call instance methods
print(blu.sing("Happy"))
print(woo.dance)
