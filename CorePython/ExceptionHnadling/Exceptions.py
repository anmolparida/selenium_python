import sys

def exceptionHandling1():
    try:
        a = 10
        b = 20 #'string'
        c = 0

        d = (a + b) / c

        print(d)

    except ValueError:
        print(sys.exc_info()[0])

    except TypeError:
        print('Type Error: can not operate on string to integer', sys.exc_info[0])

    except (ZeroDivisionError, TypeError):
        print(sys.exc_info()[0])

    except:
        print('If no exception is defined, by default prints this')
        raise Exception('This ia an Exception')

    else:
        print('Because there was no exception, else was executed')

    finally:
        # Works like clear all, we can do all clean up in the finally block
        print('finally block is Always Executed')


exceptionHandling1()

print('*#' * 20)

def exceptionHandling2():
    try:
        a = 100
        b = '5'
        c = 0

        e = a + b
        print(e)

        d = a /c
        print(d)

    except ValueError:
        print(sys.exc_info()[0])

    except (TypeError, ZeroDivisionError):
        print(sys.exc_info()[0])
       # handle multiple exceptions
       # TypeError and ZeroDivisionError

    except:
        print('Exception Not Defined')
        print(sys.exc_info()[0])


exceptionHandling2()