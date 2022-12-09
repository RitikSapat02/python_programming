class account:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited amount is {amount}\n")
        print(self.__str__())

    def withdrawal(self,amount):
        if(amount <= self.balance):
            self.balance-=amount
            print("Withdrawal accepted")
            print(f"withdrawal amount is {amount}\n")
            print(self.__str__())
        
        else:
            print("Balance is not that much!!")
        
    def __str__(self):
        return f"owner: {self.owner}\nBalance: {self.balance}"

a = account("raj",45000)
print(a)

a.withdrawal(40000)
a.deposit(234543493481000000)
