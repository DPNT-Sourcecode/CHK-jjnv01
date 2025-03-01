from collections import Counter
from math import floor

individual_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10, 
    "G": 20, 
    "H":10, 
    "I":35, 
    "J":60, 
    "K":70, 
    "L":90, 
    "M":15, 
    "N":40, 
    "O":10, 
    "P":50, 
    "Q":30, 
    "R":50, 
    "S":20,
    "T":20,
    "U":40,
    "V":50,
    "W":20,
    "X":17,
    "Y":20,
    "Z":21 
}

special_offers = {"A": [(3, 130), (5, 200)], 
                  "B": [(2, 45)], 
                  "H": [(5, 45), (10, 80)], 
                  "K":[(2, 120)], 
                  "P":[(5, 200)], 
                  "Q":[(3, 80)], 
                  "V":[(2, 90), (3, 130)]
                  }

whole_cart_offers = {"E": (2, "B"), 
                     "F":(2, "F"), 
                     "N":(3, "M"), 
                     "R":(3, "Q"), 
                     "U":(3, "U")
                     }

group_offers = {"STXYZ":(3, 45)
}

def checkout(skus):
    if not isinstance(skus, str):
        return -1
    try:
        group_offers_applied = find_group_offer(skus)
        item_counter = group_offers_applied[0]
        running_price = group_offers_applied[1]
        items = multiitem_offers(item_counter)
        final_price = running_price
        for item in items:
            final_price += itemcost(item, items[item])
    except ValueError:
        return -1
    return final_price


def find_best_offer(item_name, amount, all_offers):
    best_offer_amount, best_offer_price = 0, None
    if item_name in special_offers:
        for i in range(len(all_offers[item_name])):
            offer_amount = all_offers[item_name][i][0]
            offer_price = all_offers[item_name][i][1]
            if offer_amount <= amount and offer_amount > best_offer_amount:
                best_offer_price = offer_price
                best_offer_amount = offer_amount
    return best_offer_amount, best_offer_price


# print(find_best_offer('A', 6, special_offers))


def find_all_offers(item_name, amount):
    offers = []
    while amount > 0:
        offer = find_best_offer(item_name, amount, special_offers)
        offer_amount = offer[0]
        offer_price = offer[1]
        if offer_price is not None:
            offers.append([offer_amount, offer_price])
            amount -= offer_amount
        else:
            break
    return offers


def itemcost(item_name, amount):
    discounted_price = 0
    offers = find_all_offers(item_name, amount)
    if offers:
        for offer in offers:
            offer_amount = offer[0]
            offer_price = offer[1]
            if amount >= offer_amount:
                number_offers = floor(amount / offer_amount)
                discounted_price += offer_price * number_offers
                amount -= number_offers * offer_amount
    final_price = amount * individual_prices[item_name] + discounted_price
    return final_price


def multiitem_offers(item_counter):
    for item in item_counter:
        if item not in individual_prices:
            raise ValueError
        for offer_item in whole_cart_offers:
            if item == offer_item and whole_cart_offers[item][1] in item_counter:
                free_item = whole_cart_offers[item][1]
                required_amount = whole_cart_offers[item][0]
                if item == offer_item and item != free_item:
                    number_discounted_items = floor(item_counter[item] / required_amount)
                else:
                    number_discounted_items = floor((item_counter[item]-1) / required_amount)
                if number_discounted_items>=item_counter[free_item]:
                    item_counter[free_item]=0
                else:
                    item_counter[free_item]-= number_discounted_items
    return item_counter

def find_group_offer(skus):
    item_counter = Counter(skus)
    selected_items=[]
    n_of_group_offers = 0
    for item in item_counter:
        if item not in individual_prices:
            raise ValueError
        for offer in group_offers:
            if item in offer:
                selected_items.extend(item*item_counter[item])
    
    if len(selected_items)==3:
        for item in selected_items:
            item_counter[item]-=1
        
        # Updating number of offers applied 
        n_of_group_offers=1
        
    elif len(selected_items)>3:
        # sorting selected items based on their price
        sorted_items = sorted(selected_items, key=lambda x: individual_prices.get(x, float('inf')), reverse=True)

        # creating groups of 3 items each in the sorted list
        groups = [sorted_items[i:i+3] for i in range(0, len(sorted_items), 3)]

        # selecting complete groups with 3 items each
        selected_groups = [i for i in groups if len(i)==3]

        # calculating the number of group offer discounts to apply
        n_of_group_offers = len(selected_groups)
        
        # deducting offered item from basket 
        for group in selected_groups:
            for item in group:
                item_counter[item]-=1
    
    # Multiplying number of group offer discounts applied by the price of that offer. 
    # TODO (beyond current test requirements):  create selected_items PER offer, use associated offer price from group_offers
    running_price = 45*n_of_group_offers
    return item_counter, running_price




        


