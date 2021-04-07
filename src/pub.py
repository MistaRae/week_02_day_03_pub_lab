from src.food import Food
from src.drink import Drink
from src.customer import Customer
import pdb

class Pub:
    def __init__(self, name, till):
         self.name = name
         self.till = till
         self.stock = []
    
    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False
        
    def is_customer_too_drunk(self, customer):
        if customer.drunkenness > 15:
            return True
        return False

    def find_stock_by_name(self, item):
        # pdb.set_trace()
        for stock_item in self.stock:
            if stock_item.name == item and stock_item.quantity > 0:
                return True
        return False


    def customer_can_afford(self, customer, item):
        if customer.wallet >= item.price:
            return True
        return False

    def remove_funds_from_wallet(self, customer):
        #customer wallet - item price
        pass

    def add_funds_to_till(self, item):
        #pub.till + item price 
        pass

    def remove_item_from_stock(self):
        #
        pass

    def add_drunkenness (self, customer):
        pass

    def remove_drunkenness (self, customer):
        pass

    def sell_item_to_customer (self, customer):
        pass