#!/usr/bin/env python3


sum = 3
digits= 3
m = 10
num = 0


# sum < digits
def two_digits(sum, m, adder=0):
    for i in range(sum):
        num = i*m + sum - i + adder
        yield num


def all_digits(sum, m, digits, adder=0):
    if digits > 2:
        for i in range(sum):
            two_digits(sum - i, digits - 1, )


def bal(sum, m, max):
   for i in range(sum):
       yield from two_digits(sum - i, m, m*i)


def next_bal(num, m, s, list):



print([i for i in two_digits(4, 10)])
#all_digits(4, 10, 3)
bal_list = [i for i in bal(4, 10, 3)]
for i in bal_list:
    print(i)


