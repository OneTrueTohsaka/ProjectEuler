# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def num_list(lower=1, upper=100):
    numbers = []
    for i in range(lower, upper + 1):
        numbers.append(i)
    return numbers


if __name__ == "__main__":
    number_list = num_list()
    total_squares = 0
    total = 0
    for j in number_list:
        total += j
        j **= 2
        total_squares += j
    total_num_squared = total**2
    print("The total of the squares = {}.".format(total_squares))
    print("The total of the numbers squared = {}.".format(total_num_squared))
    print("The difference = {}.".format(total_num_squared - total_squares))
