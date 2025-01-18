import unittest
from checkout_solution import checkout, itemcost

class TestCheckout(unittest.TestCase):
    def test_finalprice_checkout(self):
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('BBBBB'), 120)
        self.assertEqual(checkout('AAA'), 130)
        self.assertEqual(checkout('AAABBCD'), 130+45+20+15)

    def test_inptfail_checkout(self):
        self.assertEqual(checkout(3), -1)
        self.assertEqual(checkout('1'), -1)
    
    def test_totaloffer_itemcost(self):
        self.assertEqual(itemcost('B', 3), 75)
        self.assertEqual(itemcost('B', 5), 90+30)


if __name__ == '__main__':
    unittest.main()