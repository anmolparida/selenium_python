
def RemoveNthCharacter(string, n):
    return string[:n] + string[n+1:]


print(RemoveNthCharacter('Python', 0))
print(RemoveNthCharacter('Python', 3))
print(RemoveNthCharacter('Python', 5))