# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Make a program to find primes, then print the 10001st one


def make_list(lower=2, upper=120000):
    numbers = []
    for i in range(lower, upper):
        numbers.append(i)
    return numbers


def prime_sieve(number_list):
    for n in number_list:
        for x in number_list:
            if x != n and x % n == 0:
                number_list.remove(x)
    return number_list


if __name__ == "__main__":
    primes = make_list()
    answer = prime_sieve(primes)
    print(answer[10000])
