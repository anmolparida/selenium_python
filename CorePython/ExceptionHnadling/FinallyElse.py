def exceptionHandling():
    try:
        a = 10
        b = 20 #'string'
        c = 0

        d = (a + b) / c

        print(d)

    # except ZeroDivisionError:
    #     print('Division by Zero not Allowed')
    # except TypeError:
    #     print('Type Error: can not operate on string to integer')
    except:
        print('If no exception is defined, by default prints this')
        raise Exception('This ia an Exception')
    else:
        print('Because there was no exception, else was executed')
    finally:
        # Works like clear all, we can do all clean up in the finally block
        print('finally block is Always Executed')


exceptionHandling()