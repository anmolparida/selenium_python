# Interviwer : Kumar Gaurav


# Remove Word With Repeat Letters

inputArr = ["abcd", "aabc", "deca", "zese"]

for word in inputArr:
    x = list(set(word))
    if len(x) == len(word):
        print(word)


# Count Occurrences Of Character In List

vStr = "mississippi"

d = {}
for letter in vStr:
    # if letter.isalpha():
        if letter not in d.keys():
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
print(d)





