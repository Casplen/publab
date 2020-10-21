import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Keith", 2000)
        self.customer2 = Customer("John", 2000)

        self.drink1 = Drink("Guinness", 550)
        self.drink2 = Drink("G+T", 400)
        drinks = [self.drink1, self.drink2]

        self.pub = Pub("Red_Lion", 10000, drinks)


    def test_pub_has_a_name(self):
        self.assertEqual("Red_Lion", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(10000, self.pub.till)

    
    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))


    def test_add_cash(self):
        self.pub.add_cash(200)
        self.assertEqual(10200, self.pub.till)

    def test_remove_cash(self):
        self.pub.remove_cash(200)
        self.assertEqual(9800, self.pub.till)
    
    def test_increase_drinks_sold(self):
        self.pub.increase_drinks_sold()
        self.assertEqual(1, self.pub.drinks_sold)

