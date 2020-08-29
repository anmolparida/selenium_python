"""
Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
        arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal.

Find the Possible words in the list the from the set of characters

"""

wordList = ["go","bat","me","eat","goal","boy", "run"]
charList = ['e','o','b', 'a','m','g', 'l']

def possibleWords_method1(wordList, charList):
    output = []
    # present = True
    for word in wordList:
        outerCount = len(word)
        innerCount = 0
        for letter in word:
            if letter in charList:
                innerCount = innerCount + 1
        if innerCount == outerCount:
            output.append(word)
    return  output


print(possibleWords_method1(wordList, charList))




def possibleWords_method2(wordList, charList):

    def charCount(word):
        dict = {}
        for i in word:
            if i in dict.keys():
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        return dict

    for word in wordList:
        flag = 1
        chars = charCount(word)

        for key in chars:
            if key not in charList:
                flag = 0
            else:
                if charList.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)


possibleWords_method2(wordList, charList)





wordList = ["go","bat","me","eat","goal","boy", "run"]
charList = ['e','o','b', 'a','m','g', 'l']

