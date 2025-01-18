from lib.solutions.SUM import sum_solution
import unittest

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(2,3), 5)



