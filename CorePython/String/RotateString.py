#  Write a Python program to change a given string to a new string where the first and last chars have been exchanged
def rotate_string(vStr, step):
    print(vStr)


# rotate_string('abcd')
# rotate_string('12345')


def character_exchange(vStr: str):
    print(vStr[-1:] + vStr[1:-1] + vStr[:1])


character_exchange('abcd')
character_exchange(12345)