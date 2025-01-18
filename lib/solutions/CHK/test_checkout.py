import unittest
from collections import Counter
from checkout_solution import checkout, itemcost, multiitem_offers, find_all_offers

class TestCheckout(unittest.TestCase):
    def test_finalprice_checkout(self):
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('BBBBB'), 120)
        self.assertEqual(checkout('AAABBCD'), 130+45+20+15)
        self.assertEqual(checkout('EEB'), 80)

        # self.assertEqual(30, checkout('B'))
    
    def test_checkout_invalid_inputs(self):
        self.assertEqual(checkout(3), -1)
        self.assertEqual(checkout('1'), -1)
        self.assertEqual(checkout('!@#'), -1)
        self.assertEqual(checkout(''), 0)  # No items

    def test_itemcost(self):
        # self.assertEqual(calculate_cost('B', 2), 45)
        self.assertEqual(itemcost('B', 3), 75)
        self.assertEqual(itemcost('B', 5), 90+30)
        self.assertEqual(itemcost('A', 10), 200 + 200)  
        self.assertEqual(itemcost('C', 2), 40) 

    def test_find_all_offers(self):
        self.assertEqual(find_all_offers('A', 10), [[5, 200], [5, 200]])

    def test_multiitem(self):
        expected_return = Counter('EEB')
        self.assertEqual(multiitem_offers(Counter('EEBB')), expected_return)

if __name__ == '__main__':
    unittest.main()

