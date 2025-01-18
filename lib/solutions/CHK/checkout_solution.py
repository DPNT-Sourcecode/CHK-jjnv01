from collections import Counter
from math import floor

individual_prices = {
    'A':50, 
    'B':30, 
    'C':20, 
    'D':15,
    'E': 40,
}

special_offers = {
    'A':[(3, 130), (5,200)], 
    'B':[(2, 45)],  
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    items = Counter(skus)
    final_price = 0
    try:
        for item in items:
            final_price+=itemcost(item, items[item])
    except ValueError:
        return -1
    return final_price

def itemcost(item: str, amount: int):
    if item not in individual_prices.keys():
        raise ValueError("Item not available")
    
    total_offer = 0
    breakpoint()
    if product, offers in special_offers.items():
        special_offer_item = special_offers[product][0]
        special_offer_price = special_offers[product][1]

        if amount>=special_offer_item:
            offers = floor(amount/special_offer_item)
            total_offer+=special_offer_price*offers
            amount-=offers*special_offer_item
    
    item_cost = total_offer + (amount*individual_prices[item])
    return item_cost


def find_best_offer(item_name, amount):
    best_offer = None
    possible_offers = special_offers[item_name]
    


