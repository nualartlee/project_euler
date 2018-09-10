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


if __name__ == '__main__':
    unittest.main()
