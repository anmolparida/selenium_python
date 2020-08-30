print("""
POLYMORPHISM
""")
class Maharashtra:

    def stateLocation(self):
        print("State in West India")


class Odisha:
    def stateLocation(self):
        print("State in East India")


Maharashtra().stateLocation()
Odisha().stateLocation()

print("""
ENCAPSULATION
""")

class Maharashtra:

    __capital = 'Mumbai'

    def getCapital(self):
        print('Capital of Maharashtra is',Maharashtra.__capital)

    def setCapital(self, newCapital):
        Maharashtra.__capital = newCapital

m = Maharashtra()
m.getCapital()

__capital = 'Bombay'
m.getCapital()

m.setCapital('Bombay')
m.getCapital()


print("""
INHERITANCE
""")

class India:

    def __init__(self):
        print("India is Incredible")

    def language(self):
        print('India speaks Multiple Languages')

    def population(self):
        print('India population is 1.2  Billion')

class Maharashtra():

    def __init__(self):
        print("Pune is city in Maharashtra")

    def language(self):
        print('Maharashtra speaks Marathi')

    def population(self):
        print('Maharashtra population is 12 Million')

class Pune(Maharashtra, India):

    def __init__(self):
        super().__init__()  # By default Super calls the first argument - parent class
        Maharashtra.__init__(self)  # Explicitly calling in case of multiple inheritance
        India.language(self)
        Maharashtra.language(self)

    def population(self):
       print('Pune population is 7 Million')

        # print('Pune population is 7 Million')



m = Maharashtra()
p = Pune()


p.language()
p.population()