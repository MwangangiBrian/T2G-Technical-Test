"""Question 3: Design a function that takes a string or sequence of characters as input and returns the character
that appears most frequently. //Eg 11189 => '1' //hello => l"""


def char_freq(sequence):
    count = {}
    for char in sequence:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return max(count, key=count.get)

# use case
# print(char_freq("11189"))
# print(char_freq("Weareworkingtohavenewupdatepackagesavailableforyoursystem"))
