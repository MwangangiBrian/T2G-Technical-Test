"""
Question 6:Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
for his unique way of speaking. He often reverses the order of words in his
sentences. For example, instead of saying "I am home" he might say "Home
am I" Design a function that takes a sentence as input and returns a new
sentence with the words reversed in the same order that Master Yoda would use.
"""


def reverse_words(sentence):
    words = sentence.split(' ')
    reversed_words = words[::-1]
    # bring the words together
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Use case
# s = "Master Yoda, a renowned Jedi Master from the Star Wars universe"
# print(reverse_words(s))