import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer_1 = Customer("Mark", 10.00, 33, 0)
        self.customer_2 = Customer("Andrew", 20.00, 17, 10)
        self.customer_3 = Customer("Steven", 50.00, 37, 20)
   
    def test_customer_setup(self):
        self.assertEqual("Mark", self.customer_1.name)
        self.assertEqual(10.00, self.customer_1.wallet)
        self.assertEqual(33, self.customer_1.age)
        self.assertEqual(0, self.customer_1.drunkenness)