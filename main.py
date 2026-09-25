class BankAccount:
    Bank_Name = "Bank of America"

    def __init__(self):
        self.customer_name="Bethany"
        self.current_balance=200
        self.minimum_balance=0
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
class Savings_account(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest.rate=0.02

    def add_interest(self):
        interest=self.current_balance+self.interest.rate
        self.current.balance+=interest


account1 = BankAccount()
account1.deposit(100)
account1.withdraw(50)

account2=BankAccount()
account2.deposit(200)
account2.withdraw(80)


account1.print_customer_information()
account2.print_customer_information()