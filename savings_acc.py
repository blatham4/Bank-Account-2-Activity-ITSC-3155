class Savings_account(BankAccount):
    def __init__(self, customer_name, account_number, routing_number):
        super().__init__(customer_name, account_number, routing_number)
        self.interest_rate=0.02

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest

    def print_customer_information(self):
        super().print_customer_information()
        print("Interest Rate:"+ str(self.interest_rate))
