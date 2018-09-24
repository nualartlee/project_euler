#!/usr/bin/env python3

import datetime
import math


def balance_right(number, base):
    """
    Return the next balanced number in descending order,
    reducing only the right side.
    (It is assumed that this is possible)

    :param number: The number in base-10.
    :param base: The base number representation.
    :return: The new balanced number in base-10.
    """
    # Single digit is already balanced
    if math.log(number, base) < 1:
        return number

    # The number is already balanced
    left_sum = get_left_sum(number, base)
    right_sum = get_right_sum(number, base)
    diff = right_sum - left_sum
    if diff == 0:
        return number

    digit_list = get_basex_digit_list(number, base)
    half = get_half_digits(number, base)

    # The right side is smaller: rearrange to make larger
    if diff < 0:

        # Find the largest digit that will have to decrease
        # taking into account the sum value and base system
        digit_to_decrease = left_sum // (base - 1) + 1
        if digit_list[-digit_to_decrease] < left_sum % (base - 1):
            digit_to_decrease += 1
            while digit_list[-digit_to_decrease] == 0:
                digit_to_decrease += 1
        # Prepare list if decreasing more than one digit
        if digit_to_decrease > 1:
            for i in range(1, digit_to_decrease):
                digit_list[-i] = base - 1
            digit_list[-digit_to_decrease] -= 1
        new_number = get_base10_value(digit_list, base)
        diff = get_right_sum(new_number, base) - get_left_sum(new_number, base)

    # Subtract from right until balanced
    for i in range(half):
        index = -i -1
        if digit_list[index] >= diff:
            digit_list[index] -= diff
            break
        else:
            diff -= digit_list[index]
            digit_list[index] = 0
    return get_base10_value(digit_list, base)


def can_balance_right(number, base):
    """
    Check if it is possible to balance the given number without
    decreasing the left hand side.

    :param digit_list: The number to balance as a list of digits.
    :param base: The base number representation.
    :return: True if it is possible.
    """
    half = get_half_digits(number, base)
    # True if central digit > 0 (or single digit)
    if get_central_digit(number, base):
        if get_digit_value(get_central_digit(number, base), number, base) > 0:
            return True
    # True if right is larger than left
    left_sum = get_left_sum(number, base)
    right_sum = get_right_sum(number, base)
    if right_sum >= left_sum:
        return True
    # True if right sum can be made greater
    digit_list = get_basex_digit_list(number, base)
    for i in range(half):
        if digit_list[i - half] > 0:
            max_right = digit_list[i - half] - 1 + (base - 1) * (half - i - 1)
            return max_right >= left_sum
    return False


def decrease_left(number, base):
    """
    Decrease the left hand side by the smallest amount possible.
    (Set right to zero and subtract 1)

    :param digit_list: The number as a list of digits.
    :param base: The base number representation.
    :return: The new decreased number as a list of digits.
    """
    bottom_half_digits = math.ceil(math.log(number, base) / 2)
    modulo = base ** bottom_half_digits
    number -= number % modulo
    return number - 1


def decrease_right(number, base):
    """
    Decrease the right hand side by the smallest amount possible
    (Decrease the number by one).

    :param digit_list: The number as a list of digits.
    :param base: The base number representation.
    :return: The new decreased number as a list of digits.
    """
    return number - 1


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


def get_basex_digit_list(number, base):
    """
    Get the representation of a base-10 number in the given base
    as a list of digits.

    :param n: The base-10 number to translate (int).
    :param base: The base number representation to translate to.
    :return: The translated number as a list of digits.
    """
    digit_list = []
    while number > 0:
        digit_list.insert(0, number % base)
        number = number // base
    return digit_list


def get_central_digit(number, base):
    """
    Get the index of the central digit.

    :param number: The number in base-10
    :param base: The base number representation
    :return: The index of the central digit or None if even
    """
    digits = math.ceil(math.log(number, base))
    if not digits % 2:
        return None
    return digits // 2


def get_digit_value(digit, number, base):
    """
    Get the base-10 value of a digit in a base-n number.

    :param digit: The digit number.
    :param number: The number in base-10.
    :param base: The base number representation.
    :return: Base-10 value of that digit.
    """
    result = (number // base ** digit) % base
    return result


def get_half_digits(number, base):
    """
    Get the number of digits that should be balanced.
    (Does not include central shared digit if odd numbered)

    :param digits: The number as a list of digits.
    :return: The number of digits that should be balanced.
    """
    half = math.ceil(math.log(number, base)) // 2
    if half == 0:
        return 1
    return half


def get_left_sum(number, base):
    """
    Get the sum of the left hand side digits.
    (does not include central digit)

    :param number: The number in base-10.
    :return: The sum value of the left hand side digits.
    """
    bottom_half_digits = math.ceil(math.log(number, base) / 2)
    half_number = number // base ** bottom_half_digits
    result = 0
    while half_number:
        result += half_number % base
        half_number //= base
    return result


def get_next_balanced_desc(number, base):
    """
    Get the next balanced number in descending order.

    :param digit_list: Starting number in base-10, will return this if balanced.
    :param base: The base number representation.
    :return: The next balanced number in descending order in base-10.
    """
    if not number:
        return None
    if can_balance_right(number, base):
        new_number = balance_right(number, base)
        return new_number
    else:
        return get_next_balanced_desc(decrease_left(number, base), base)


def get_right_sum(number, base):
    """
    Get the sum of the right hand side digits.
    (Does not include central digit)

    :param number: The number in base-10.
    :return: The sum value of the right hand side digits.
    """
    digits = math.log(number, base)
    if digits < 1:
        return number
    bottom_half_digits = math.ceil(digits) // 2
    half_number = number % base ** bottom_half_digits
    result = 0
    while half_number:
        result += half_number % base
        half_number //= base
    return result


def get_result(digit_list, base, modulo):
    """
    Get the result as expected.

    :param digit_list: The initial number as a list of digits.
    :param base: The base number representation.
    :param modulo: The modulo to use to reduce answer.
    :return: The string with the two values expected.
    """
    number = get_base10_value(digit_list, base)
    start = datetime.datetime.now()
    total = 0
    sum_value = 0
    next_value = get_next_balanced_desc(number, base)
    previous_value = 0
    while next_value:
        print("{0}\t{1}".format(next_value, next_value - previous_value))
        previous_value = next_value
        total = (total + 1) % modulo
        sum_value = (sum_value + next_value) % modulo
        next_value = get_next_balanced_desc(next_value - 1, base)
    stop = datetime.datetime.now()
    print(stop - start)
    return "{0} {1}".format(total, sum_value)


if __name__ == "__main__":
    import fileinput
    modulo = 1004535809
    data_input = fileinput.input()
    line1 = data_input[0].split()
    base = int(line1[0])
    digits = int(line1[1])
    digit_str_list = data_input[1].split()
    digit_list = [int(x) for x in digit_str_list]
    print(get_result(digit_list, base, modulo))
