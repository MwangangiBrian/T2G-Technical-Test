"""
Question 5:Design a function that takes a list of integers as input. The function should
return True if the list contains two consecutive threes (3 next to a 3) anywhere
within the list. Otherwise, it should return False. For example, the function
should return True for [1, 3, 3] and False for [1, 3, 1, 3].
"""


def consecutive_threes(num_list):
    for i in range(len(num_list) - 1):
        if num_list[i] == 3 and num_list[i + 1] == 3:
            return True
    return False


# Use case
a, b = [1, 3, 3], [1, 3, 1, 3]
print(consecutive_threes(a),consecutive_threes(b))
