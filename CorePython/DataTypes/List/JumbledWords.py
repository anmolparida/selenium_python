from itertools import permutations

def words(letters):
    for n in range(1, len(letters)+1):
        yield from map(''.join, permutations(letters, n))

for word in words('ABC'):
    print(word)