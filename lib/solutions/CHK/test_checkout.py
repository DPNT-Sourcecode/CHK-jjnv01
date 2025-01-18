import unittest
from collections import Counter
from checkout_solution import (
    checkout,
    itemcost,
    multiitem_offers,
    find_all_offers,
    find_best_offer,
    special_offers,
)


class TestCheckout(unittest.TestCase):
    def test_finalprice_checkout(self):
        self.assertEqual(checkout("B"), 30)
        self.assertEqual(checkout("BBBBB"), 120)
        self.assertEqual(checkout("AAABBCD"), 130 + 45 + 20 + 15)
        self.assertEqual(checkout("EEB"), 80)

        # self.assertEqual(30, checkout('B'))

    def test_checkout_invalid_inputs(self):
        self.assertEqual(checkout(3), -1)
        self.assertEqual(checkout("1"), -1)
        self.assertEqual(checkout("!@#"), -1)
        self.assertEqual(checkout(""), 0)  # No items

    def test_itemcost(self):
        # self.assertEqual(calculate_cost('B', 2), 45)
        self.assertEqual(itemcost("B", 3), 75)
        self.assertEqual(itemcost("B", 5), 90 + 30)
        self.assertEqual(itemcost("A", 10), 200 + 200)
        self.assertEqual(itemcost("C", 2), 40)

    def test_find_best_offer(self):
        # Test finding the best single offer
        self.assertEqual(find_best_offer("A", 6, special_offers), (5, 200))
        self.assertEqual(find_best_offer("A", 3, special_offers), (3, 130))
        self.assertEqual(find_best_offer("B", 1, special_offers), (0, None))
        self.assertEqual(find_best_offer("Z", 5, special_offers), (0, None))

    def test_find_all_offers(self):
        self.assertEqual(find_all_offers("A", 10), [[5, 200], [5, 200]])

    def test_multiitem(self):
        self.assertEqual(multiitem_offers(Counter("EEBB")), Counter({"E": 2, "B": 1}))
        self.assertEqual(multiitem_offers(Counter("EEEEBB")), Counter({"E": 4, "B": 0}))
        self.assertEqual(multiitem_offers(Counter("EEB")), Counter({"E": 2, "B": 0}))
        self.assertEqual(multiitem_offers(Counter("EEBBB")), Counter({"E": 2, "B": 2}))

    def test_edge_cases(self):
        # Test edge cases for various functions
        self.assertEqual(checkout('AAABBBCCC'), 130 + 45 + 60)  # Mixed items
        self.assertEqual(checkout(''), 0)  # Empty cart
        self.assertRaises(ValueError, itemcost, 'X', 1)  # Invalid item
        self.assertEqual(find_all_offers('B', 0), [])  # No items to apply offers


if __name__ == "__main__":
    unittest.main()



