"""
Write a Python function that takes a list of words and returns the length of the longest one

"""
def find_longest_word_method1(input_list):
    max_len = 0
    longest = ""
    for word in input_list:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    print(longest)


find_longest_word_method1(["PHP", "Exercises", "Backend"])


def find_longest_word_method2(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort(reverse=False)
    print(word_len)
    print(word_len[-1][1])


find_longest_word_method2(["PHP", "Exercises", "Backend"])