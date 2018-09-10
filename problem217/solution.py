#!/usr/bin/env python3


def balance_right(digit_list, base):
    """
    Return the next balanced number reducing only the rigth side.
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
    Check if it is possible to balance the number reducing only the right side.
    """
    if len(digit_list) == 1:
        return True
    left_sum = get_left_sum(digit_list)
    right_sum = get_right_sum(digit_list)
    if right_sum >= left_sum:
        return True
    half = get_half_digits(digit_list)
    for i in range(half):
        if digit_list[i - half] > 0:
            max_right = digit_list[i - half] - 1 + (base - 1) * (half - i - 1)
            return max_right >= left_sum


def decrease_left(digit_list, base):
    """
    Decrease the left hand side.
    """
    print(len(digit_list))
    half = get_half_digits(digit_list)
    # Find the smallest non-zero digit to decrease
    for i in range(1, half + 1):
        if digit_list[-half - i] > 0:
            digit_list[-half - i] -= 1
            for j in range(half + i):
                digit_list[-j] = base - 1
            break
    return digit_list


def decrease_right(digit_list, base):
    """
    Decrease the right hand side (decrease the number by 1).
    """
    decreased = get_base10_value(digit_list, base) - 1
    return get_basex_digit_list(decreased, base)


def get_base10_value(digit_list, base):
    value = 0
    for i in range(len(digit_list)):
        value += digit_list[i] * base ** (len(digit_list) - i - 1)
    return value


def get_basex_digit_list(n, base):
    """
    Get a digit_list representation for the number n in the given base.
    """
    digit_list = []
    while n > 0:
        digit_list.insert(0, n % base)
        n = n // base
    return digit_list


def get_half_digits(digits):
    half = len(digits) // 2
    if half == 0:
        return 1
    return half


def get_left_sum(digit_list):
    half = get_half_digits(digit_list)
    return sum(digit_list[:half])


def get_next_balanced_desc(digit_list, base):
    if can_balance_right(digit_list, base):
        balance_right(digit_list, base)
        yield digit_list
        return get_next_balanced_desc(decrease_right(digit_list, base), base)
    else:
        return get_next_balanced_desc(decrease_left(digit_list, base), base)


def get_right_sum(digit_list):
    half = get_half_digits(digit_list)
    return sum(digit_list[-half:])


if __name__ == "__main__":
    import fileinput
    modulo = 1004535809
    data_input = fileinput.input()
    line1 = data_input[0].split()
    base = int(line1[0])
    digits = int(line1[1])
    digit_str_list = data_input[1].split()
    digit_list = [int(x) for x in digit_str_list]
    base10_value = get_base10_value(digit_list, base)
    # print(base10_value)
    balanced_list = [i for i in get_next_balanced_desc(digit_list, base)]
    print(balanced_list)
    print("{0} {1}".format(len(balanced_list) % modulo, sum(balanced_list) % modulo))

