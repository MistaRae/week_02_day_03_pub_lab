import unittest 
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00) 
        self.customer_1 = Customer("Mark", 10.00, 33, 0)
        self.customer_2 = Customer("Andrew", 20.00, 17, 10)
        self.customer_3 = Customer("Steven", 50.00, 37, 20)

    def test_pub_setup(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual([], self.pub.stock)

    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer_1))
        self.assertEqual(False, self.pub.check_age(self.customer_2))

    def test_is_customer_too_drunk(self):
        self.assertEqual