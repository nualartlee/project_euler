#!/usr/bin/env python3


def balance_right(digit_list, base):
    """
    Return the next balanced number in descending order,
    reducing only the right side.
    (It is assumed that this is possible)

    :param digit_list: The number as a list of digits.
    :param base: The base number representation.
    :return: The new balanced number as a list of digits.
    """
    if len(digit_list) == 1:
        return digit_list
    left_sum = get_left_sum(digit_list)
    right_sum = get_right_sum(digit_list)
    diff = right_sum - left_sum
    half = get_half_digits(digit_list)

    # The number is already balanced
    if diff == 0:
        return digit_list

    # The right side is smaller: rearrange to make larger
    if diff < 0:

        # Find the largest digit that will have to decrease
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
        diff = get_right_sum(digit_list) - get_left_sum(digit_list)

    # Subtract from right until balanced
    for i in range(half):
        index = -i -1
        if digit_list[index] >= diff:
            digit_list[index] -= diff
            break
        else:
            diff -= digit_list[index]
            digit_list[index] = 0
    return digit_list


def can_balance_right(digit_list, base):
    """
    Check if it is possible to balance the given number without
    decreasing the left hand side.

    :param digit_list: The number to balance as a list of digits.
    :param base: The base number representation.
    :return: True if it is possible.
    """
    # True if it is a single digit
    if len(digit_list) == 1:
        return True
    # True if right is larger than left
    left_sum = get_left_sum(digit_list)
    right_sum = get_right_sum(digit_list)
    if right_sum >= left_sum:
        return True
    # True if central digit > 0
    half = get_half_digits(digit_list)
    if len(digit_list) % 2 and digit_list[half] > 0:
        return True
    # True if right sum can be made greater
    for i in range(half):
        if digit_list[i - half] > 0:
            max_right = digit_list[i - half] - 1 + (base - 1) * (half - i - 1)
            return max_right >= left_sum


def decrease_left(digit_list, base):
    """
    Decrease the left hand side by the smallest amount possible.

    :param digit_list: The number as a list of digits.
    :param base: The base number representation.
    :return: The new decreased number as a list of digits.
    """
    half = get_half_digits(digit_list)
    # Find the smallest non-zero digit to decrease
    for i in reversed(range(half)):
        if digit_list[i] > 0:
            digit_list[i] -= 1
            digit_list[i+1:] = [base-1] * len(digit_list[i+1:])
            break
    value = get_base10_value(digit_list, base)
    digit_list = get_basex_digit_list(value, base)
    return digit_list


def decrease_right(digit_list, base):
    """
    Decrease the right hand side by the smallest amount possible
    (Decrease the number by one).

    :param digit_list: The number as a list of digits.
    :param base: The base number representation.
    :return: The new decreased number as a list of digits.
    """
    decreased = get_base10_value(digit_list, base) - 1
    return get_basex_digit_list(decreased, base)


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


def get_basex_digit_list(n, base):
    """
    Get the representation of a base-10 number in the given base
    as a list of digits.

    :param n: The base-10 number to translate (int).
    :param base: The base number representation to translate to.
    :return: The translated number as a list of digits.
    """
    digit_list = []
    while n > 0:
        digit_list.insert(0, n % base)
        n = n // base
    return digit_list


def get_half_digits(digits):
    """
    Get the number of digits that should be balanced.
    (Does not include central shared digit if odd numbered)

    :param digits: The number as a list of digits.
    :return: The number of digits that should be balanced.
    """
    half = len(digits) // 2
    if half == 0:
        return 1
    return half


def get_left_sum(digit_list):
    """
    Get the sum of the left hand digits.

    :param digit_list: The number as a list of digits.
    :return: The sum value of the left hand side digits.
    """
    half = get_half_digits(digit_list)
    return sum(digit_list[:half])


def get_next_balanced_desc(digit_list, base):
    """
    Get the next balanced number.

    :param digit_list: Starting number as a digit list, will return this if balanced.
    :param base: The base number representation.
    :return: The next balanced number in descending order as a digit list.
    """
    if not digit_list:
        return
    if can_balance_right(digit_list, base):
        balance_right(digit_list, base)
        yield get_base10_value(digit_list, base)
        yield from get_next_balanced_desc(decrease_right(digit_list, base), base)
    else:
        yield from get_next_balanced_desc(decrease_left(digit_list, base), base)


def get_right_sum(digit_list):
    """
    Get the sum of the right hand digits.

    :param digit_list: The number as a list of digits.
    :return: The sum value of the right hand side digits.
    """
    half = get_half_digits(digit_list)
    return sum(digit_list[-half:])


def get_result(digit_list, base, modulo):
    """
    Get the result as expected.

    :param digit_list: The initial number as a list of digits.
    :param base: The base number representation.
    :param modulo: The modulo to use to reduce answer.
    :return: The string with the two values expected.
    """
    total = 0
    sum_value = 0
    for i in get_next_balanced_desc(digit_list, base):
        total = (total + 1) % modulo
        sum_value = (sum_value + i) % modulo
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

