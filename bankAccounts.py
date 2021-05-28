class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        # your code here! (remeber, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount): # increases the account balance by the given amount
        self.balance += amount
        return self
    
    def withdraw(self, amount): # decreases the account balance by the givena amount if there are sufficient funds; if there is not 
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insuffucient funds: Charging a $2.50 fee")
            self.balance -= 2.50
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

account1 = BankAccount(0.003, 200)
account2 = BankAccount(0.15, 1100)
account1.deposit(100).deposit(100).deposit(50).withdraw(75).yield_interest().display_account_info()
account2.deposit(555).deposit(1500).deposit(382).withdraw(25).withdraw(50).withdraw(75).withdraw(100).yield_interest().display_account_info()