# Problem 4: A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# 9009 = 91 x 99

num_list = []
palindrome_list = []


def is_palindrome(number):
    if number[0] == number[-1] and number[1] == number[-2] and number[2] == number[-3]:
        return True


for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        z = str(z)
        num_list.append(z)


for i in num_list:
    if is_palindrome(i):
        i = int(i)
        palindrome_list.append(i)
        print(i)
print("The highest 6 digit palindrome is: " + str(max(palindrome_list)))

# b = 0
#
# for i in range(100,999):
#     for n in range (100,999):
#         y = i * n
#         if y > b and str(y) == str(y)[::-1]:
#             b = y
#
# print(b)
