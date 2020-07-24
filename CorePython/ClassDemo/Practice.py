
class Fruit(object):

    def __init__(self):
        print('Fruit object initiated')

    def nutrition(self):
        print('nutrition value for the fruit')

    def fruit_shape(self):
        print('shape of the fruit')



class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print('Apple class initiated')

    def nutrition(self):
        print('nutrition value of orange is Vitamin C')

    def color(self):
        print('Color of Orange is orange')


f = Fruit()
f.nutrition()
f.fruit_shape()

print('\n')

o = Orange()
o.nutrition()
o.fruit_shape()
o.color()

