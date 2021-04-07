import unittest 
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00) 
        self.customer_1 = Customer("Mark", 10.00, 33, 0)
        self.customer_2 = Customer("Andrew", 20.00, 17, 10)
        self.customer_3 = Customer("Steven", 0.00, 37, 20)
        self.drink_1 = Drink("Whisky", 5, 5, 10)
        self.drink_2 = Drink("Punk IPA",4.50, 1, 10)
        self.food_1 = Food("Pie", 2.75, 5, 10)
        self.food_2 = Food("Crisps", 0.99, 1, 0)
            
            

    def test_pub_setup(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual([], self.pub.stock)

    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer_1))
        self.assertEqual(False, self.pub.check_age(self.customer_2))

    def test_is_customer_too_drunk(self):
        self.assertEqual(True, self.pub.is_customer_too_drunk(self.customer_3))
        self.assertEqual(False, self.pub.is_customer_too_drunk(self.customer_1))

    def test_find_stock_by_name_drink(self):
        self.pub.stock.extend([self.drink_1, self.drink_2, self.food_1, self.food_2])
        self.assertEqual(True, self.pub.find_stock_by_name("Whisky"))
        self.assertEqual(False, self.pub.find_stock_by_name("Crisps"))

    def test_customer_can_afford(self):
        self.assertEqual(True, self.pub.customer_can_afford(self.customer_1, self.drink_1))
        self.assertEqual(False, self.pub.customer_can_afford(self.customer_3, self.drink_1))

    def test_remove_funds_from_wallet(self):
        self.assertEqual()