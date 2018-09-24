#!/usr/bin/env python3

from datetime import datetime


def get_two_digit_sum_table(m):
    """
    For each possible digit sum value:
    Return the list of numbers (up to two digits) whose digit sum equals a given value.

    :param m: Base number system
    :return: A list of lists where each sublist contains all the numbers whose digit sum equals
    the index of the sublist
    """
    table = []
    for i in range(2 * m - 1):
        table.append([number for number in two_digit_sum_generator(i, m)])
    return table


def two_digit_sum_generator(sum, m):
    """
    Return all the numbers (up to 2 digits) whose digit sum equals the given value.

    :param sum: Value of the sum of the number's digits
    :param m: Base number system
    :return: The next number in increasing order
    """
    if sum >= m:
        number = (sum - (m - 1)) * m + (m - 1)
    else:
        number = sum
    for _ in range(m - abs(m - sum - 1)):
        yield number
        number += (m - 1)


def two_digit_sum_lookup(sum, two_digit_sum_table, adder=0):
    """
    Look up all the numbers (up to 2 digits) whose digit sum equals the given value.

    :param sum: Value of the sum of the number's digits
    :param two_digit_sum_table: A table with the lists of all posible two digit sums (see get_two_digit_sum_table)
    :param adder: And additional value to add to each returned number
    :return: The next number in increasing order
    """
    for num in two_digit_sum_table[sum]:
        yield num + adder


def x_digit_sum_generator(sum, m, two_digit_sum_table, x, adder=0):
    """
    Return all the numbers (up to x digits) whose digit sum equals the given value.

    :param sum: Value of the sum of the number's digits
    :param m: Base number system
    :param two_digit_sum_table: A table with the lists of all posible two digit sums (see get_two_digit_sum_table)
    :param x: Number of digits
    :param adder: And additional value to add to each returned number
    :return: The next number in increasing order
    """

    # If more than 2 digits:
    if x > 2:

        # Minimum (start) value for this digit must be large enough to reach the digit sum
        start = 0
        required_digits = sum // (m - 1)
        if required_digits == x:
            start = m - 1
        if required_digits == x - 1:
            start = sum % (m - 1)

        # Reduce and recurse until only two digits are left
        for i in range(start, m if sum > (m - 1) else sum + 1):
            yield from x_digit_sum_generator(sum - i, m, two_digit_sum_table,  x - 1, adder + i * m ** (x-1))

    # If only two digits: return from two_digit_sum
    else:
        yield from two_digit_sum_lookup(sum, two_digit_sum_table, adder)


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

    # Get the table with the two-digit sums:
    tds_table = get_two_digit_sum_table(m)

    # One digit numbers
    for i in range(1, m):
        yield i

    # Two digit numbers
    for i in range(1, m):
        yield i*m + i

    # Three digit numbers
    for i in range(1, m):
        for j in range(m):
            yield i*m**2 + j*m + i

    # Larger numbers
    digits = 4
    while True:
        #print("{} digit values:\n\n".format(digits))
        half = digits // 2
        odd = digits % 2

        # If the number of total digits is odd
        if odd:

            # For each possible left hand side
            for left in range(m ** (half-1), m ** (half)):
                digit_sum = get_digit_sum(left, m)

                #print("left: {}".format(left))
                #print("digit sum: {}".format(digit_sum))

                # For each possible central digit
                for j in range(m):

                    # For each right hand side equalling the digit sum
                    for right in x_digit_sum_generator(digit_sum, m, tds_table, half):
                        yield left * m ** (half + 1) + j * m ** half + right

        # If the number of total digits is even
        else:

            # For each possible left hand side
            for left in range(m ** (half-1), m ** (half)):
                digit_sum = get_digit_sum(left, m)

                #print("left: {}".format(left))
                #print("digit sum: {}".format(digit_sum))

                # For each right hand side equalling the digit sum
                for right in x_digit_sum_generator(digit_sum, m, tds_table, half):
                    yield left * m ** half + right

        digits += 1


maxim = 10 ** 8
start = datetime.now()
for i in balanced_number_generator(10):
    if i > maxim:
        break
print(datetime.now() - start)

#for j in range(20):
#    print([i for i in two_digit_sum(j, 11)])
#print([i for i in two_digit_sum(9, 10, strict=True)])
#for i in x_digit_sum(12, 10, 3):
#    print(i)
#print('\n\n')
#for i in x_digit_sum(9, 10, 3, strict=True):
#    print(i)
#bal_list = [i for i in bal(4, 10, 3)]
#for i in bal_list:
#    print(i)


