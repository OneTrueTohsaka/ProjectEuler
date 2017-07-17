# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import functools
import math

lel = functools.reduce(lambda x, y: x*y//math.gcd(x, y), range(1, 21))
print(lel)
print(2520*2520)
