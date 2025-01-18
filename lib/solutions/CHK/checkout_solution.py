from collections import Counter
from math import floor

individual_prices = {
    'A':50, 
    'B':30, 
    'C':20, 
    'D':15
}

special_offers = {
    'A':(3, 130), 
    'B':(2, 45)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    items = Counter(skus)
    final_price = 0
    for item in items:
        final_price+=itemcost(item, items[item])
    return final_price

def itemcost(item, amount):
    if item not in individual_prices.keys():
        raise ValueError("Item not available")
    
    total_offer = 0

    if item in special_offers:
        special_offer_item = special_offers[item][0]
        special_offer_price = special_offers[item][1]

        if amount>=special_offer_item:
            offers = floor(amount/special_offer_item)
            total_offer+=special_offer_price*offers
            amount-=offers*special_offer_item
    
    item_cost = total_offer + (amount*individual_prices[item])
    return item_cost

