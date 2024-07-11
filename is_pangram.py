"""
Question 4:Design a function that determines whether a given string is a pangram. A
pangram is a sentence or phrase containing every letter of the alphabet at
least once. Punctuation and case are typically ignored. For example, the
string "The quick brown fox jumps over the lazy dog" is a pangram, while
"Hello, world!" is not.
"""


def is_pangram(sentence):
    sentence = set(sentence.lower())
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    # compare characters on the alphabet to the sentence
    return alpha.issubset(sentence)

# use case
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("Hello World"))
