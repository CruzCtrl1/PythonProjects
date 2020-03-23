class changeMachine:
    def __init__(self, amount = 0):
        self.amount = amount #assume this is a string. convert to a float?
        self.quarters = 0
        self.dimes = 0
        self.nickels = 0
        self.pennies = 0
    def calculate(self):
        while self.amount > 0:
            if ((self.amount-0.25) >= 0):
                self.amount -= 0.25
                self.quarters += 1
            elif((self.amount-0.10) >= 0):
                self.amount -= 0.10
                self.dimes += 1
            elif((self.amount-0.05) >= 0):
                self.amount -= 0.05
                self.nickels += 1
            else:
                self.amount -= 0.01
                self.pennies += 1
    def results(self):
        print('Your change consists of the following:')
        print(f'There are {self.quarters} quarters')
        print(f'There are {self.dimes} dimes')
        print(f'There are {self.nickels} nickels')
        print(f'There are {self.pennies} pennies')