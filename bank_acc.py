
class BankAccount:
    Bank_Name = "Bank of America"

    def __init__(self, customer_name, account_number, routing_number):
        self.customer_name=customer_name
        self.current_balance=200
        self.minimum_balance=0
        self.__account_number = account_number
        self.__routing_number = routing_number
        
    def deposit(self, amount):
        if amount>0 :
            self.current_balance=amount+self.current_balance
        else:
            print("Can not deposit negative amount")

    def withdraw(self, amount):
        if amount < 0:
            print("Can not withdraw negative amount")
        elif self.current_balance - amount < self.minimum_balance:
            print("Can not withdraw because it would go below the minimum balance")
        else:
            self.current_balance = self.current_balance - amount
    def print_customer_information(self):
        print("Bank Name:",self.Bank_Name)
        print("Customer Name:",self.customer_name)
        print("Current Balance:",self.current_balance)
        print("Minimum Balance:",self.minimum_balance)