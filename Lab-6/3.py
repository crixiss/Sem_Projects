class BankAccount:
    def __init__(self,account_number,balance=0):
        self.__account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Rs{amount} deposited successfully")
    def withdraw(self,amount):
        if(amount>self.__balance):
            print("insufficient balance")
        else:
            self.__balance-=amount
            print(f"Rs{amount} withdrawn successfully")
    def get_account_details(self):
        print("Account Details:")
        print(f"Account Number:{self.__account_number}\n Balance:{self.__balance}")
a1=BankAccount("1234abcd",500)
a1.get_account_details()
a1.deposit(1000)
a1.withdraw(1000)
a1.withdraw(700)
a1.get_account_details()
