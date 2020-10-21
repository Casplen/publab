class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.drinks_sold = 0

    
    def add_cash(self, cash):
        self.till += cash

    def remove_cash(self, cash):
        self.till -= cash

    def increase_drinks_sold(self):
        self.drinks_sold += 1

