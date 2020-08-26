"""
Write a Python program to count the number of characters (character frequency) in a string.
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

"""

def numberOfCharacters(vStr, ignoreCase):
    if ignoreCase == 'YES':
        vStr = vStr.upper()

    d = {}
    for letter in vStr:
        if letter not in d.keys():
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
    print(d)


numberOfCharacters('MISSIssipPI', 'NO')
numberOfCharacters('MISSIssipPI', 'YES')
