# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# Use Euclid's formula

# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2

# a = m ** 2 - n ** 2
#
# b = 2 * m * n
#
# c = m ** 2 + n ** 2

m = 0
n = 0


for i in range(1, 25):
    for j in range(1, 25):
        # if i > j > 0:

            a = i ** 2 - j ** 2
            b = 2 * i * j
            c = i**2 + j**2
            # print(a, b, c)
            if (a + b + c) == 1000:
                print(a, b, c, a * b * c)
