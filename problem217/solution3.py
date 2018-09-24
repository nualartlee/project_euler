#!/usr/bin/env python3


sum = 3
digits= 3
m = 10
num = 0

t_d_s = [
    [0],
    [1, 10],
    [2, 11, 20],
    [3, 12, 21, 30],
    [4, 13, 22, 31, 40],
    [5, 14, 23, 32, 41, 50],
    [6, 15, 24, 33, 42, 51, 60],
    [7, 16, 25, 34, 43, 52, 61, 70],
    [8, 17, 26, 35, 44, 53, 62, 71, 80],
    [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],
    [19, 28, 37, 46, 55, 64, 73, 82, 91],
    [29, 38, 47, 56, 65, 74, 83, 92],
    [39, 48, 57, 66, 75, 84, 93],
    [49, 58, 67, 76, 85, 94],
    [59, 68, 77, 86, 95],
    [69, 78, 87, 96],
    [79, 88, 97],
    [89, 98],
    [99],
]

def two_digit_sum(sum, m, adder=0):
    #print("two digits: {0} {1} {2}".format(sum, m, adder))
    if sum >= m:
        number = (sum - (m - 1)) * m + (m - 1)
    else:
        number = sum
    for _ in range(m - abs(m - sum - 1)):
        yield number + adder
        number += (m - 1)


def x_digit_sum(sum, m, x, adder=0):
    if x > 2:
        for i in range(sum + 1):
            yield from x_digit_sum(sum - i, m,  x - 1, adder + i * m ** (x-1))
    else:
        yield from two_digit_sum(sum, m, adder)


def get_digit_sum(number, base):
    """
    get the sum of the digits
    """
    result = 0
    while number:
        result += number % base
        number //= base
    return result


def balanced_number_generator(m):

    # one digit
    for i in range(1, m):
        yield i

    # two digits
    for i in range(1, m):
        yield i*m + i

    # three digits
    for i in range(1, m):
        for j in range(m):
            yield i*m**2 + j*m + i

    # more digits
    digits = 4
    while True:
        print("{} digit values:\n\n".format(digits))
        import pdb;pdb.set_trace()
        half = digits // 2
        odd = digits % 2

        # If the number of total digits is odd
        if odd:

            # For each possible left hand side
            for left in range(m ** (half-1), m ** (half)):
                digit_sum = get_digit_sum(left, m)

                print("left: {}".format(left))
                print("digit sum: {}".format(digit_sum))

                # For each possible central digit
                for j in range(m):

                    # For each right hand side equalling the digit sum
                    for right in x_digit_sum(digit_sum, m, half):
                        yield left * m ** (half + 1) + j * m ** half + right

        # If the number of total digits is even
        else:

            # For each possible left hand side
            for left in range(m ** (half-1), m ** (half)):
                digit_sum = get_digit_sum(left, m)

                print("left: {}".format(left))
                print("digit sum: {}".format(digit_sum))

                # For each right hand side equalling the digit sum
                for right in x_digit_sum(digit_sum, m, half):
                    yield left * m ** half + right

        digits += 1



prev = 0
#for i in balanced_number_generator(10):
#    print(i)
#    if i <= prev:
#        print('          smaller')
#        break
#    prev = i

#for j in range(20):
#    print([i for i in two_digit_sum(j, 11)])
#print([i for i in two_digit_sum(9, 10, strict=True)])
#for i in x_digit_sum(9, 10, 3):
#    print(i)
#print('\n\n')
#for i in x_digit_sum(9, 10, 3, strict=True):
#    print(i)
#bal_list = [i for i in bal(4, 10, 3)]
#for i in bal_list:
#    print(i)


