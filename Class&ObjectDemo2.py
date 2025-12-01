class MyAccount:

    def __init__(self):
            print("Object Created Succesfully !!")
    
    def set_AccountNumber(self, accountNumber , balance):
        self.accountNumber = accountNumber
        self.balance = balance
    
    def get_AccountNumber(self):
        print("Account Number : ",self.accountNumber)
        print("Balance : ",self.balance)
        print("----------------------")

    def deposit(self, amount):
        self.balance += amount
        print(amount , " of amount deposited Successfully  \nTotal Balanace :",self.balance)

    def withdrow(self,amount):
        if(self.balance <= amount):
            print("Not Suficient Amount in your Account ",self.balance," Do not Withdrow")
        else:
            self.balance -= amount
            print(amount," is Withdrow Successfully !\n Total Balance  := ",self.balance)



    def get_balance(self):
        print("Account Balance : ", self.balance)

# main function 

m1 = MyAccount()
m1.set_AccountNumber(123456,500)
m1.get_AccountNumber()
m1.deposit(1000)
m1.withdrow(500)
m1.withdrow(100)