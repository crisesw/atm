class Account:
    def __init__(self, id, balance):
        self.balance = balance
        self.id = id

    def get_id(self):
        return self.id

    def get_balance(self):
        return self.balance
    
    def deposit(self, d):
        self.balance += d
        print("Deposit : $", d)
        print("Balance : $", self.balance)
    
    def withdraw(self, w):
        if self.balance < w:
            print("Not Enough Balance... Plz Check..")
            print("Balance : $", self.balance)
        else:
            self.balance -= w
            print("Withdraw : $", w)
            print("Balance : $", self.balance)
        