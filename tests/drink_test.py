import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Whisky", 5.00, 5)

    def test_drink_has_name(self):
        self.assertEqual("Whisky", self.drink_1.name)