import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer_1 = Customer("Mark", 10.00, 0)
        self.customer_2 = Customer("Andrew", 20.00, 10)
        self.customer_3 = Customer("Steven", 50.00, 20)
   
    def test_customer_has_name(self):
        self.assertEqual("Mark", self.customer_1.name)