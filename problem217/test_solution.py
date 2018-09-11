#!/usr/bin/env python3

import unittest
import solution


class TestSolution(unittest.TestCase):

    def test_balance_right(self):
        digit_list = [1]
        base = 10
        correct = [1]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [9]
        base = 10
        correct = [9]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 2]
        base = 10
        correct = [1, 1]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 9]
        base = 10
        correct = [1, 1]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 2, 3]
        base = 10
        correct = [1, 2, 1]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 2, 3, 4]
        base = 10
        correct = [1, 2, 3, 0]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 2, 3, 4, 0, 2]
        base = 10
        correct = [1, 2, 3, 4, 0, 2]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 2, 8, 4, 0, 2]
        base = 10
        correct = [1, 2, 8, 3, 8, 0]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 9, 8, 4, 0, 2]
        base = 10
        correct = [1, 9, 8, 3, 9, 6]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 9, 8, 1, 1, 1]
        base = 10
        correct = [1, 9, 8, 0, 9, 9]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 9, 8, 0, 0, 1, 1, 1, 0, 0]
        base = 10
        correct = [1, 9, 8, 0, 0, 1, 1, 0, 9, 7]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 9, 8, 0, 0, 0, 1, 1, 1, 0, 0]
        base = 10
        correct = [1, 9, 8, 0, 0, 0, 1, 1, 0, 9, 7]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 9, 8, 0, 0]
        base = 20
        correct = [1, 9, 7, 10, 0]
        result = solution.balance_right(digit_list, base)
        self.assertEqual(result, correct)

    def test_can_balance_right(self):
        digit_list = [2]
        base = 10
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, True)
        digit_list = [2, 1]
        base = 10
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, False)
        digit_list = [1, 1]
        base = 10
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, True)
        digit_list = [1, 2]
        base = 10
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, True)
        digit_list = [4, 5, 6, 7, 8]
        base = 10
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, True)
        digit_list = [9, 8, 0, 6, 5]
        base = 10
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, False)
        digit_list = [34, 23, 0, 0, 39, 8, 9]
        base = 40
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, True)
        digit_list = [34, 23, 0, 6, 39, 8, 9, 4]
        base = 40
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, True)
        digit_list = [33, 39, 38, 28, 1, 8, 9, 4]
        base = 40
        result = solution.can_balance_right(digit_list, base)
        self.assertEqual(result, False)

    def test_decrease_left(self):
        digit_list = [1, 1, 0, 1, 0, 1, 0, 1]
        base = 10
        correct = [1, 1, 0, 0, 9, 9, 9, 9]
        result = solution.decrease_left(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 0, 0, 0, 0, 1, 0, 1]
        base = 10
        correct = [0, 9, 9, 9, 9, 9, 9, 9]
        result = solution.decrease_left(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 0, 1, 0, 0, 1, 0, 1]
        base = 20
        correct = [1, 0, 0, 19, 19, 19, 19, 19]
        result = solution.decrease_left(digit_list, base)
        self.assertEqual(result, correct)

    def test_decrease_right(self):
        digit_list = [1, 1, 0, 1, 0, 1, 0, 1]
        base = 10
        correct = [1, 1, 0, 1, 0, 1, 0, 0]
        result = solution.decrease_right(digit_list, base)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0, 1, 0, 0, 0]
        base = 10
        correct = [1, 1, 0, 0, 9, 9, 9]
        result = solution.decrease_right(digit_list, base)
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
        digit_list = [1]
        correct = 1
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1]
        correct = 1
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0]
        correct = 1
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0, 1]
        correct = 2
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [3, 1, 1, 0, 1]
        correct = 2
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [4, 3, 1, 1, 0, 1]
        correct = 3
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [3, 4, 3, 1, 1, 0, 1]
        correct = 3
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)
        digit_list = [2, 3, 4, 3, 1, 1, 0, 1]
        correct = 4
        result = solution.get_half_digits(digit_list)
        self.assertEqual(result, correct)

    def test_get_left_sum(self):
        digit_list = [1]
        correct = 1
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1]
        correct = 1
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0]
        correct = 1
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0, 1]
        correct = 2
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [3, 1, 1, 0, 1]
        correct = 4
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [4, 3, 1, 1, 0, 1]
        correct = 8
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [3, 4, 3, 1, 1, 0, 1]
        correct = 10
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [2, 3, 4, 3, 1, 1, 0, 1]
        correct = 12
        result = solution.get_left_sum(digit_list)
        self.assertEqual(result, correct)

    def test_get_right_sum(self):
        digit_list = [1]
        correct = 1
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1]
        correct = 1
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0]
        correct = 0
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [1, 1, 0, 1]
        correct = 1
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [3, 1, 1, 0, 1]
        correct = 1
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [4, 3, 1, 1, 0, 1]
        correct = 2
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [3, 4, 3, 1, 1, 0, 1]
        correct = 2
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)
        digit_list = [2, 3, 4, 3, 1, 1, 0, 1]
        correct = 3
        result = solution.get_right_sum(digit_list)
        self.assertEqual(result, correct)


if __name__ == '__main__':
    unittest.main()
