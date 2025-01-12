class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debit" )
        print("total balance = ", self.get_balance())
    def credit(self , amount):
        self.balance += amount
        print("Rs", amount , "was credit")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 72738869)
acc1.debit(1000)
acc1.credit(200000)
print(acc1.balance)
print(acc1.account)






