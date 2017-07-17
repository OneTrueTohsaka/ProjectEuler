# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# def get_divisor_list(lower_limit=1, upper_limit=21):
#     divisor_list = []
#     for i in range(lower_limit, upper_limit):
#         divisor_list.append(i)
#     return divisor_list
#
#
# def find_lcm(step=2520):
#     while True:
#         for i in range(step, step ** 2, step):
#             for j in get_divisor_list():
#
#
#
# if __name__ == "__main__":
#
#     answer = find_lcm()
#     print(answer)
#

import functools
import math

lel = functools.reduce(lambda x, y: x*y//math.gcd(x, y), range(1, 21))
print(lel)
print(2520*2520)
