import unittest 
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food_1 = Food("Pie", 2.50, 10)

    def test_food_has_name(self):
        self.assertEqual("Pie", self.food_1.name)