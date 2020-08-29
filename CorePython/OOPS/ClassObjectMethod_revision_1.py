class Parrot:

    # class attribute
    species = 'bird'

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return self.name, song

    def dance(self):
        return self.name


#instantiate parrot class
blu = Parrot('Blu', 10)

# access the class attributes
print(blu.species)
print(blu.__class__.species)

# accessing the instance attribute
print(blu.name)
print(blu.age)

# calling instance attribute
print(blu.sing('Happy Happy'))
print(blu.dance())

