# Object Oriented Programming
# class name - camel case starting with Capital letter


class Car(object):
    # define methods
    # define attribute
    # init is needed to boot up the class, like a constructor in Java

    wheels = 4 # member variables, class attributes

    def __init__(self, make, model = '550i'):
        self.makeOfCar = make  # can be anything : make or makeOfCar is same
        self.make = make
        self.model = model


    def info(self):
        print('Make of the Car: ' + self.make)
        print('Model of the Car: ' + self.make)



print(Car.wheels, '\n')

c1 = Car('BMW', '550i')
print(c1.make, c1.model, c1.wheels)
c1.info()
c1.wheels = 6
print(c1.wheels)

c2 = Car('Benz', 'E350')
print(c2.make, c2.model, c2.wheels)
c2.info()
print('\n')
print(c2.info()) # prints both print inside the method inside the class followed by None


