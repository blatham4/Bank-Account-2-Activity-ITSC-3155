
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, account_number,routing_number, transfer_limit):
        super().__init__(customer_name, account_number, routing_number)
        self.transfer_limit=transfer_limit

    def transfer(self, amount):
        if amount > self.transfer_limit:
            print("Transfer amount exceeds the transfer limit")
        elif amount < 0:
            print("Can not transfer negative amount")
        elif self.current_balance - amount < self.minimum_balance:
            print("Can not transfer because it would go below the minimum balance")
        else:
            self.current_balance = self.current_balance - amount

    def print_customer_information(self):
        super().print_customer_information()
        print("Transfer Limit:", self.transfer_limit)
