# import module sys to get the type of exception
import sys

def exception1(inputList):
    for entry in randomList:
        try:
            print("The entry is", entry)
            r = 1/int(entry)
            break
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Next entry.")
            print()
    print("The reciprocal of", entry, "is", r)


randomList = ['a', 0, 2]
# exception1(randomList)



def exception2(inputList):
    for entry in randomList:
        try:
            print("The entry is", entry)
            r = 1/int(entry)
            break
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            print("Next entry.")
            print()
    print("The reciprocal of", entry, "is", r)


randomList = ['a', 0, 2]
exception2(randomList)