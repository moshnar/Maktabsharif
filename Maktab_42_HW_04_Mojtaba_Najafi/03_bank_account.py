class Account:
    def __init__(self,name,balance):# initialis varibales
        self.name = name
        self.balance = balance
        self.min_balance = 10

    def deposit(self,amount): # make a deposit
        self.balance += amount
        print("Deposit was successful!")

    def withdraw(self,amount):# make a withdraw considering the minimum balance
        if self.__withdrawable(amount):

            self.balance -= amount
            print("Withdraw was successful!")
        else :
            print(f'Maximum withdraw is {self.balance - self.min_balance}')


    def transfer(self, amount, name): # make a transfer considering the minimum balance
        if self.__withdrawable(amount):

            self.balance = self.balance - amount
            name.balance = name.balance + amount
            print(f"transfer was successful and the new balance is {self.balance}")
        else:
            print(f'Maximum transfer amount is {self.balance - self.min_balance}')




    def __withdrawable(self,amount): # checks if the amount exceeded the minimum balance

        if self.balance - amount > self.min_balance:
            return True
        else:
            return False

a = Account('Person1',1000)
b = Account('Person2', 2500)

a.withdraw(1000)
a.transfer(500,b)

print(a.balance)
print(b.balance)
a.transfer(50,b)
a.transfer(500,b)