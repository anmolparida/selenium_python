"""
Sort with custom function using key - useful for sorting Strings
"""
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# print vowels
print('Sorted vowels list:', vowels.sort())     # returns None
vowels.sort()
print('Sorted vowels list:', vowels)     # returns None

vowels = ['e', 'a', 'u', 'o', 'i']
print('Sorted vowels list:', sorted(vowels))    # returns ['a', 'e', 'i', 'o', 'u']

numbers = [11, 51, 23, 6]
print('Sorted vowels list ASC:', sorted(numbers))
print('Sorted vowels list DESC:', sorted(numbers, reverse=True))
alphanum = [11, 51, 23, 6, 'A', 'B', 'C' ]
# print('Sorted vowels list:', sorted(alphanum))   # TypeError: '<' not supported between instances of 'str' and 'int'


vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(key=len)
print('sorted with keys',vowels)

print('\nGeeksForGeeks')
# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = "python"
print('String - sorted based on ASCII translations:',x, sorted(x))

# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print('Dict - sorted based on ASCII translations:',x, sorted(x))

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))

# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print(sorted(x))

# list with words and chars
vowels = ['aaaa', 'bbb', 'e', 'ddd', 'cccc']
print('sorted with out key',sorted(vowels))
print('sorted with len key',sorted(vowels, key=len))

# list with char only
vowels = ['e', 'a', 'u', 'o', 'i']
print('sorted with out key',sorted(vowels))
print('sorted with len key',sorted(vowels, key=len)) # no change in order as all elements are of len 1

## list with numbers and key as a method

def remainder(number):
    return  number % 7

lst = [15, 3, 11, 7]

print('regular sort',sorted(lst))
print('sorted DESC with key', sorted(lst, key=remainder))
print('sorted ASC with key', sorted(lst, key=remainder, reverse=True))

