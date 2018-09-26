#!/usr/bin/env python3

from datetime import datetime


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
        half = digits // 2
        odd = digits % 2

        # If the number of total digits is odd
        if odd:

            # For each possible left hand side
            for left in range(m ** (half-1), m ** (half)):
                digit_sum = get_digit_sum(left, m)

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

                # For each right hand side equalling the digit sum
                for right in x_digit_sum_generator(digit_sum, m, tds_table, half):
                    yield left * m ** half + right

        digits += 1


def balanced_number_result(m, max_digits):

    num_count = 0
    num_sum = 0

    # Get the table with the two-digit sums:
    tds_table = two_digit_sum_result_table(m)

    # One digit numbers
    num_count += m - 1
    num_sum += ((m - 1) * m) // 2

    # Two digit numbers
    num_count += m - 1
    num_sum += ((m + 1) + ((m-1) * m - (m - 1)) * (m - 1)) // 2

    # Three digit numbers
    num_count += (m - 1) * m
    # Middle digit sum
    num_sum += ((m - 1)**2 * m) // 2
    # Side digit sum
    num_sum += ((m - 1) * m // 2) * (m**2 + 1)

    # Larger numbers
    digits = 4
    while digits <= max_digits:
        half = digits // 2
        odd = digits % 2

        # If the number of total digits is odd
        if odd:

            # For each possible left hand side
            for left in range(m ** (half-1), m ** (half)):
                digit_sum = get_digit_sum(left, m)

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

                # For each right hand side equalling the digit sum
                for right in x_digit_sum_generator(digit_sum, m, tds_table, half):
                    yield left * m ** half + right

        digits += 1


def get_base10_value(digit_list, base):
    """
    Get the value in base-10 representation.

    :param digit_list: The number to translate as a list of digits.
    :param base: The base number representation.
    :return: The base-10 representation as an int.
    """
    value = 0
    for i in range(len(digit_list)):
        value += digit_list[i] * base ** (len(digit_list) - i - 1)
    return value


def get_digit_sum(number, base):
    """
    get the sum of the digits
    """
    result = 0
    while number:
        result += number % base
        number //= base
    return result


def get_two_digit_sum_table(m):
    """
    For each possible digit sum value:
    Return the list of numbers (up to two digits) whose digit sum equals a given value.

    :param m: Base number system
    :return: A list of lists where each sublist contains all the numbers whose digit sum equals
    the index of the sublist
    """
    start = datetime.now()
    table = []
    for i in range(2 * m - 1):
        table.append([number for number in two_digit_sum_generator(i, m)])
    print("Table creation:")
    print(datetime.now() - start)
    return table


def solution(digit_list, base, modulo):
    """
    Get the result as expected.

    :param digit_list: The initial number as a list of digits.
    :param base: The base number representation.
    :param modulo: The modulo to use to reduce answer.
    :return: The string with the two values expected.
    """
    limit = get_base10_value(digit_list, base)
    total = 0
    sum_value = 0

    for number in balanced_number_generator(base):
        if number > limit:
            break
        total = (total + 1) % modulo
        sum_value = (sum_value + number) % modulo
    return "{0} {1}".format(total, sum_value)


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


def two_digit_sum_result(sum, m):
    """
    Return the possibility count and total for two digits adding to the given sum.

    :param sum: Value of the sum of the two digits
    :param m: Base number system
    :return: (x, y) tuple where x = number count and y = sum of all numbers.
    """
    # Calculate possibilities
    c = m - abs(m - sum - 1)

    # Calculate sum
    s2 = 0
    if sum < m:
        s2 = (((c - 1) * c) // 2) * (m + 1)
    else:
        s2 = (m**3 - m) // 2
        d = sum - m + 1
        diff = (((d - 1) * d) // 2) * (m + 1)
        s2 -= diff

    return c, s2


def two_digit_sum_result_table(m):
    """
    For each possible digit sum value:
    Return the count and total of numbers (up to two digits) whose digit sum equals a given value.

    :param m: Base number system
    :return: List of tuples (x, y) where x is the number count and y the total.
    Index of the list indicates digit sum.
    """
    result = []
    for i in range(2 * m - 1):
        result.append(two_digit_sum_result(i, m))
    return result


def x_digit_sum_result_table(m, digits, previous_table):
    """

    :param m:
    :param digits:
    :param previous_table:
    :return:
    """
    table = []
    # Intersection with previous table
    for i in range(m * (digits - 1) - 1):
        c = sum([previous_table[i][0] for i in range(m * (digits - 1) - 1 - i)])
        s = sum([previous_table[i][1] for i in range(m * (digits - 1) - 1 - i)])
        table.append((c, s))
    # Additional sums beyond previous table
    for i in range(m * digits -1):
        c = 1
        s = i * m * digits + previous_table[m * (digits - 1) - 2][1]

    return table



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


def x_digit_sum_result(sum, m, two_digit_sum_table, x, multiplier=1):
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
        required_digits = sum // (m - 1)
        # All digits maxed out
        if required_digits == x:
            return 1 * multiplier, (m ** (x + 1) - 1) * multiplier
        # All but one digit maxed out
        elif required_digits == x - 1:
            start = sum % (m - 1)
        # At least one free digit
        else:
            start = 0

        # Number of possibilities this digit adds (multiplier of possibilities for subsequent digits)
        if sum > (m - 1):
           multiplier *= m - start
        else:
            multiplier *= sum + 1 - start

        # Reduce and recurse until only two digits are left
        return x_digit_sum_generator(sum - i, m, two_digit_sum_table,  x - 1, multiplier)

    # If only two digits: return from two_digit_sum
    else:
        yield from two_digit_sum_lookup(sum, two_digit_sum_table, adder)


if __name__ == "__main__":
    import fileinput
    modulo = 1004535809
    data_input = fileinput.input()
    line1 = data_input[0].split()
    base = int(line1[0])
    digits = int(line1[1])
    digit_str_list = data_input[1].split()
    digit_list = [int(x) for x in digit_str_list]
    start = datetime.now()
    print(solution(digit_list, base, modulo))
    print(datetime.now() - start)

    m = 10
    start = datetime.now()
    table = get_two_digit_sum_table(m)
    print(datetime.now() - start)
    j = 0
    for i in table:
        print("{0} {1} {2}".format(len(i), sum(i), i))
        j = sum(i)

    print('\n\n')

    start = datetime.now()
    t2 = two_digit_sum_result_table(m)
    t3 = x_digit_sum_result_table(m, 3, t2)
    for i in t3:
        print(i)


    for i in range(2 * m - 1):
        #c, s = two_digit_sum_result(i, m)
        #print("{0} {1} {2}".format(i, c, s))
        pass
    print(datetime.now() - start)


