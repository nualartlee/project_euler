import fileinput
import itertools


def get_half_digits(digits):
    if digits % 2 == 1:
        return int(digits/2) + 1
    return int(digits/2)


def get_even_digit_balanced_numbers(half_digits, base, limit):
    """
    Get the list of balanced numbers with the given number of half-digits and base.
    
    For each unit added to the right hand side, we can add a unit to any of the digits on the left
    while keeping balance. Iterate over all possible right hand side values (base ** half_digits)
    and for each one iterate over the left hand side digits adding the balancing unit to it.
    (That is a poor explanation...)   
    """
    for number_right in range(1, base ** half_digits):
        for partition in get_partitions(get_basex_digit_list(number_right, base)):
            while len(partition) < half_digits:
                partition.insert(0, 0)
            for cpartition in itertools.permutations(partition):
                number_left = get_base10_value(partition, base) * base ** half_digits
                number = number_left + number_right
                if number > limit:
                    continue
                yield number
            
            
    
def get_partitions(digit_list):
    for partition in get_partitions_breadth_first(digit_list):
        yield from get_partitions_depth_first(partition)

        
def get_partitions_breadth_first(digit_list):
    yield digit_list.copy()
    new_partitions = 0
    for i in reversed(range(1, len(digit_list))):
        while digit_list[i] +1 < digit_list[i-1]:
            digit_list[i-1] -= 1
            digit_list[i] += 1
            new_partitions += 1
            yield digit_list.copy()

            
def get_partitions_depth_first(digit_list):
    yield digit_list.copy()
    new_partitions = 0
    for i in reversed(range(1, len(digit_list))):
        if digit_list[i] < digit_list[i-1]:
            digit_list[i-1] -= 1
            digit_list[i] += 1
            new_partitions += 1
    if new_partitions == 0:
        return
    yield from get_partitions_depth_first(digit_list)
        

def get_odd_digit_balanced_numbers(half_digits, base, limit):
    for i in range(base):
        for number_right in range(1, base ** half_digits):
            for partition in get_partitions(get_basex_digit_list(number_right, base)):
                number_left = get_base10_value(partition, base) * base ** (half_digits + 1)
                number = number_left + i * base ** half_digits + number_right
                if number > limit:
                    continue
                yield number


def get_balanced_list(digits, base, limit):
        
    numbers = set()
    
    if base > limit:
        numbers.update([i for i in range(1, limit +1)])
    else:
        numbers.update([i for i in range(1, base)])
    
    for i in range(2, digits + 1):
        
        # The number of digits that should be balanced (includes the shared central digit if it is an odd num)
        half_digits = get_half_digits(i)
        
        if i % 2 == 0:
            print("getting {} digits even".format(i))
            numbers.update(get_even_digit_balanced_numbers(half_digits, base, limit=limit))
        else:
            print("getting {} digits odd".format(i))
            numbers.update(get_odd_digit_balanced_numbers(half_digits-1, base, limit=limit))
        print(sorted(numbers))
    return sorted(numbers)


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
        

modulo = 1004535809
data_input = fileinput.input()
line1 = data_input[0].split()
base = int(line1[0])
digits = int(line1[1])
digit_str_list = data_input[1].split()
digit_list = [int(x) for x in digit_str_list]
base10_value = get_base10_value(digit_list, base)
#print(base10_value)
balanced_list = get_balanced_list(digits, base, base10_value)
#print(balanced_list)
print([i for i in itertools.permutations([0,1,0])])
print("{0} {1}".format(len(balanced_list) % modulo, sum(balanced_list) % modulo))
