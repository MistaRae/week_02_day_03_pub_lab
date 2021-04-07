import unittest 
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food_1 = Food("Pie", 2.50, 10, 10)

    def test_food_setup(self):
        self.assertEqual("Pie", self.food_1.name)
        self.assertEqual(2.50, self.food_1.price)
        self.assertEqual(10, self.food_1.rejuvenation_level)
        self.assertEqual(10, self.food_1.quantity)