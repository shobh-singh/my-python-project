class account:
    def __init__(self , bal,acc_no):
        self.balance=bal
        self.account_no=acc_no
    
    def debit(self , amount):
        self.balance-=amount
        print("Rs. ",amount, " debited")
        print("amount ", self.get_balance())

    def credit(self , amount):
        self.balance+=amount
        print("Rs. ",amount, " credit")
        print("amount ", self.get_balance())

    def get_balance(self):
        return self.balance
    

s2=account(10000,1234)
s2.debit(1000)
s2.credit(500)

