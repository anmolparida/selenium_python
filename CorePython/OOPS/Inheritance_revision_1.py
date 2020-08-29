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

    def drive(self):
        super(BMW, self).drive()  # is same as  super().drive()
        print('You are  driving a BMW, Enjoy')

    def headup_display(self):
        print('This is a unique feature')


#
# c = Car()
# c.drive()
# c.stop()


b = BMW()
b.drive()
b.stop()
b.headup_display()
