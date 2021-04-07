import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        # I think we need to add a quantity variable so we can say that there are x amount of drink_1 available
        # otherwise we're going to have to repeat the code below alot : Customer purchases drink_1, price removed from customer.wallet, drink_1 removed from pub.stock... 
        # drink_1 is now gone, make sense?
        self.drink_1 = Drink("Whisky", 5.00, 5)

    def test_drink_setup(self):
        self.assertEqual("Whisky", self.drink_1.name)
        self.assertEqual(5.00, self.drink_1.price)
        self.assertEqual(5, self.drink_1.alcohol_level)