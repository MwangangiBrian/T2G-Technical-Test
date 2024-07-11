# Question 1:
# Design a function that reverses the digits of an integer. For example, 50 should become 5 and -12 should become -21.

def reverse_digits(number):
    num = abs(number)
    # convert integer to string
    num_str = str(num)
    # reverse string and eliminate any leading zeros
    reversed_str = num_str[::-1].lstrip("0")
    if number > 0:
        return int(reversed_str)
    elif number < 0:
        return -int(reversed_str)

    else:
        return number

# Use cases
# print(reverse_digits(0))
# print(reverse_digits(50))
# print(reverse_digits(-12))
