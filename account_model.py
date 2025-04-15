class Account():
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
        print(f"your bank balance is {self.get_final_balance()}")

        # Debit Method
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")
        print(f"your {amount} was Debited...")
        print(f"your balance is {self.get_final_balance()}")

        # Credit Method
    def credit(self, amount):
        self.balance += amount
        print(f"your {amount} was Credited...")
        print(f"your balance is {self.get_final_balance()}")

        # Get Final balance
    def get_final_balance(self):
        return self.balance
    
account_1 = Account(9201832920,90000) #(account-number, balance)
account_1.debit(5000) # amount debited
account_1.credit(6000) # amount credited