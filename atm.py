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
        

def bank_API_for_pin_check(pin):
    account_id = '1111'
    if pin == '1234':
        return account_id
    print("Your PIN is not correct!!")
    return None

if __name__ == "__main__":
    # Test Account List
    accounts = []
    accounts.append(Account('1111', 500))
    accounts.append(Account('2222', 1000))
    print(accounts[0].get_id())
    print(accounts[1].get_id())

    while True:

        print("---- Welcome to ATM ----")
        print("Please Insert your card and Push your PIN")
        print("Press 0 to remove a card")
        pin = input("Push The PIN Number: ")
        if pin == '0':
            print("Card Removed!!")
            break
 
        account_id = bank_API_for_pin_check(pin)
        print("account_id: ", account_id)
        if account_id == None:
            print("Wrong PIN Number... Retry...")
            continue

        for acc in accounts:
            print("acc.get_id() : ", acc.get_id())
            if account_id == acc.get_id():
                select_account = acc
                break
        #print("Wrong PIN Number... Retry...")
        #pin = input("Push The PIN Number")
        #continue

        while True:
            print("Select Menu You Want to Use")
            print("1. Balance")
            print("2. Deposit")
            print("3. WithDraw")
            print("0. Home Menu")
            select = int(input("Enter Your Selection : "))

            if select == 1:
                print("Your account balance is $", select_account.get_balance())
            elif select == 2:
                print("Your account balance is $", select_account.get_balance())
                dep = int(input("Enter amount to deposit : $"))
                select_account.deposit(dep)
            elif select == 3:
                print("Your account balance is $", select_account.get_balance())
                w = int(input("Enter amount to withdraw : $"))
                select_account.withdraw(w)
            elif select == 0:
                break

    






        