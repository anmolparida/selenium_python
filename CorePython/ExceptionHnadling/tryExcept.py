def exceptionHandling():
    try:
        a = 10
        b = 8 #'string'
        c = '10k'

        d = (a + b) / c

        print(d)

    except ZeroDivisionError:
        print('Division by Zero not Allowed')
    except TypeError:
        print('Type Error: can not operate on string to integer')
    except:
        print('In the Except block its not possible')


exceptionHandling()