from collections import Counter, defaultdict
from math import floor

individual_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

special_offers = {"A": [(3, 130), (5, 200)], "B": [(2, 45)]}

whole_cart_offers = {"E": (2, "B")}


def checkout(skus):
    if not isinstance(skus, str):
        return -1
    try:
        items = multiitem_offers(Counter(skus))
        final_price = 0
        for item in items:
            final_price += itemcost(item, items[item])
    except ValueError:
        return -1
    return final_price


def find_best_offer(item_name, amount, all_offers):
    best_offer_amount, best_offer_price = None, None
    if item_name in special_offers:
        best_offer_amount = 0
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
                number_discounted_items = floor(item_counter[item] / required_amount)

                if number_discounted_items >= item_counter[free_item]:
                    item_counter[free_item] = 0
                else:
                    item_counter[free_item] -= number_discounted_items

    return item_counter



