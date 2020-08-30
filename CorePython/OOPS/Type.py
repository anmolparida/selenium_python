s = 'this is a string'

print(s.upper())
print(s.lower())

print(type('a'))
print(type(9))
print(type(True))
print(type([1, 2, 3]))
print(type({1, 2, 3}))
print(type((1, 2, 3)))


inputStr = 'hello world'
print(list(map(str, inputStr.strip().split())))