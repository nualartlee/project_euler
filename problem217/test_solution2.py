#!/usr/bin/env python3

import unittest
import solution2 as solution


class TestSolution(unittest.TestCase):

    def test_balance_right(self):
        number = 1
        base = 10
        correct = 1
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 9
        base = 10
        correct = 9
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 12
        base = 10
        correct = 11
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 19
        base = 10
        correct = 11
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 123
        base = 10
        correct = 121
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 1234
        base = 10
        correct = 1230
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 123402
        base = 10
        correct = 123402
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 128402
        base = 10
        correct = 128380
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 198402
        base = 10
        correct = 198396
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 198111
        base = 10
        correct = 198099
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 1980011100
        base = 10
        correct = 1980011097
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        number = 19800011100
        base = 10
        correct = 19800011097
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)
        base = 20
        number = solution.get_base10_value([1, 9, 8, 0, 0], base)
        correct = solution.get_base10_value([1, 9, 7, 10, 0], base)
        result = solution.balance_right(number, base)
        self.assertEqual(result, correct)

    def test_can_balance_right(self):
        number = 2
        base = 10
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, True)
        number = 21
        base = 10
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, False)
        number = 11
        base = 10
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, True)
        number = 12
        base = 10
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, True)
        number = 45678
        base = 10
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, True)
        number = 98065
        base = 10
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, False)
        base = 40
        number = solution.get_base10_value([34, 23, 0, 0, 39, 8, 9], base)
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, True)
        base = 40
        number = solution.get_base10_value([34, 23, 0, 6, 39, 8, 9, 4], base)
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, True)
        base = 40
        number = solution.get_base10_value([33, 39, 38, 28, 1, 8, 9, 4], base)
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, False)
        base = 11
        number = 119
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, False)
        base = 11
        number = 11
        result = solution.can_balance_right(number, base)
        self.assertEqual(result, False)

    def test_decrease_left(self):
        number = 1
        base = 10
        correct = 0
        result = solution.decrease_left(number, base)
        self.assertEqual(result, correct)
        number = 11010101
        base = 10
        correct = 11009999
        result = solution.decrease_left(number, base)
        self.assertEqual(result, correct)
        number = 10000101
        base = 10
        correct = 9999999
        result = solution.decrease_left(number, base)
        self.assertEqual(result, correct)
        base = 20
        number = solution.get_base10_value([1, 0, 1, 0, 0, 1, 0, 1], base)
        correct = solution.get_base10_value([1, 0, 0, 19, 19, 19, 19, 19], base)
        result = solution.decrease_left(number, base)
        self.assertEqual(result, correct)

    def test_decrease_right(self):
        number = 1
        base = 10
        correct = 0
        result = solution.decrease_right(number, base)
        self.assertEqual(result, correct)
        number = 11010101
        base = 10
        correct = 11010100
        result = solution.decrease_right(number, base)
        self.assertEqual(result, correct)
        number = 1101000
        base = 10
        correct = 1100999
        result = solution.decrease_right(number, base)
        self.assertEqual(result, correct)

    def test_get_base10_value(self):
        digit_list = [1, 1, 0, 1]
        base = 10
        correct = 1101
        result = solution.get_base10_value(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0, 1, 7]
        base = 10
        correct = 11017
        result = solution.get_base10_value(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0, 1, 7]
        base = 20
        correct = 20**4 + 20**3 + 20 + 7
        result = solution.get_base10_value(digit_list, base)
        self.assertEqual(result, correct)

    def test_basex_digit_list(self):
        value = 1101
        base = 10
        correct = [1, 1, 0, 1]
        result = solution.get_basex_digit_list(value, base)
        self.assertEqual(result, correct)
        value = 11017
        base = 10
        correct = [1, 1, 0, 1, 7]
        result = solution.get_basex_digit_list(value, base)
        self.assertEqual(result, correct)
        value = 20**4 + 20**3 + 20 + 7
        base = 20
        correct = [1, 1, 0, 1, 7]
        result = solution.get_basex_digit_list(value, base)
        self.assertEqual(result, correct)

    def test_half_digits(self):
        number = 1
        base = 10
        correct = 1
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 11
        base = 10
        correct = 1
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 110
        base = 10
        correct = 1
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 1101
        base =10
        correct = 2
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 31101
        base = 10
        correct = 2
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 431101
        base = 10
        correct = 3
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 3431101
        base = 10
        correct = 3
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)
        number = 23431101
        base = 10
        correct = 4
        result = solution.get_half_digits(number, base)
        self.assertEqual(result, correct)

    def test_get_left_sum(self):
        number = 1
        base = 10
        correct = 1
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 11
        base = 10
        correct = 1
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 110
        base = 10
        correct = 1
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 1101
        base = 10
        correct = 2
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 31101
        base = 10
        correct = 4
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 431101
        base = 10
        correct = 8
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 3431101
        base = 10
        correct = 10
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)
        number = 23431101
        base = 10
        correct = 12
        result = solution.get_left_sum(number, base)
        self.assertEqual(result, correct)

    def test_get_next_balanced_desc(self):
        base = 11
        value = 122
        result = solution.get_next_balanced_desc(value, base)
        self.assertEqual(result, 122)
        value = 121
        result = solution.get_next_balanced_desc(value, base)
        self.assertEqual(result, 120)
        value = 119
        result = solution.get_next_balanced_desc(value, base)
        self.assertEqual(result, 108)

    def test_get_right_sum(self):
        number = 1
        base = 10
        correct = 1
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 11
        base = 10
        correct = 1
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 110
        base = 10
        correct = 0
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 1101
        base = 10
        correct = 1
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 31101
        base = 10
        correct = 1
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 431101
        base = 10
        correct = 2
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 3431101
        base = 10
        correct = 2
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 23431101
        base = 10
        correct = 3
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)
        number = 11
        base = 11
        correct = 0
        result = solution.get_right_sum(number, base)
        self.assertEqual(result, correct)

    def test_get_result(self):
        digit_list = [1, 10, 9]
        base = 11
        modulo = 1004535809
        correct = "31 2662"
        result = solution.get_result(digit_list, base, modulo)
        self.assertEqual(result, correct)


if __name__ == '__main__':
    unittest.main()
