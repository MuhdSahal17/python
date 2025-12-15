class Account:
    def __init__(self,balance):
        self.__balance = balance


    #to show the balance
    def get_balance(self):
        return self.__balance

    #(set) amount to balance   
    def deposit(self,amount):
        if amount <= 0:
            print("Cannot deposit this amount!")
            return
        else:
            self.__balance += amount
            print(f"total balance:{self.__balance}")
            return

    #(set) amount from balance
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance!")
            return
        elif amount <= 0:
            print("Cannot withdraw this amount")
            return
        else:
            self.__balance -= amount
            print(f"Total Balance:{self.__balance}")
            return



Money = Account(5000)
Money.withdraw(2000)

#show the balance
print(Money.get_balance())