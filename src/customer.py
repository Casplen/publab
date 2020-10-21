class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks_bought = 0

    def add_cash(self, cash):
        self.wallet += cash

    def remove_cash(self, cash):
        self.wallet -= cash

    def increase_drinks_bought(self):
        self.drinks_bought += 1