"""

'The quick brown fox jumps over the lazy dog.'
input : "The quick brown fox jumps over the lazy dog."
output : "dog. lazy the over jumps fox brown quick The "

"""

Vnput =  "The quick brown fox jumps over the lazy dog."


def RevertWordsInSentence(senetence):

    # No space between the words
    rev_sentence = ""
    for word in senetence.split():
        rev_sentence = word + rev_sentence
    print(rev_sentence)

    # With space between the words
    rev_list = []
    senetence = list(map(str, senetence.split()))
    for i in range(len(senetence)-1, 0, -1):
        rev_list.append(senetence[i])
    rev_sentence = " "
    print(rev_sentence.join(rev_list))

    # rev_sentence = []
    # for i in range(0, len(senetence.split()):
    #     rev_sentence.append(word)
    # print(rev_sentence)


RevertWordsInSentence("The quick brown fox jumps over the lazy dog.")