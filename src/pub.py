from src.food import Food
from src.drink import Drink
from src.customer import Customer

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
        pass

    def customer_can_afford(self, customer):
        pass

    def remove_funds_from_wallet(self, customer):
        pass

    def add_funds_to_till(self, item):
        pass

    def remove_item_from_stock(self):
        pass

    def add_drunkenness (self, customer):
        pass

    def remove_drunkenness (self, customer):
        pass

    def sell_item_to_customer (self, customer):
        pass