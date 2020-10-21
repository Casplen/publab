import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Keith", 2000)
        self.customer2 = Customer("John", 2000)

        self.drink1 = Drink("Guinness", 550)
        self.drink2 = Drink("G+T", 400)

    def test_customer_has_name(self):
        self.assertEqual("Keith", self.customer1.name)

    def test_add_cash(self):
        self.customer1.add_cash(200)
        self.assertEqual(2200, self.customer1.wallet)

    def test_remove_cash(self):
        self.customer1.remove_cash(200)
        self.assertEqual(1800, self.customer1.wallet)

    def test_increase_drinks_bought(self):
        self.customer1.increase_drinks_bought()
        self.assertEqual(1, self.customer1.drinks_bought)
    
