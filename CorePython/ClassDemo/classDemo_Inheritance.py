
# base class or parent class or super class
class Car(object):

    def __init__(self):
        print('You just created the car instance')

    def drive(self):
        print('Car Started')

    def stop(self):
        print('Car Stopped')


class BMW(Car):

    def __init__(self):

        print('\n')
        Car.__init__(self)
        print('You just created the BMW instance')




c = Car()
c.drive()
c.stop()


b = BMW()
b.drive()
b.stop()