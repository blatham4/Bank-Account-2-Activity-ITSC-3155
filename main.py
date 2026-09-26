from savings_acc import Savings_account
from checking_acc import CheckingAccount

account1 = Savings_account("Bethany", "123456789", "6000000")
account1.deposit(100)
account1.withdraw(50)
account1.add_interest()

account2=Savings_account("Srujana", "987654321", "8000001")
account2.deposit(200)
account2.withdraw(80)
account2.add_interest()

account1.print_customer_information()
account2.print_customer_information()


checking1 = CheckingAccount(
    "Alice",
    "10000000",
    "5000000",
    300
)
checking1.deposit(300)
checking1.withdraw(100)
checking1.transfer(150)

checking2 = CheckingAccount(
    "Bob",
    "2000000",
    "9000000",
    400
)
checking2.deposit(500)
checking2.withdraw(50)
checking2.transfer(200)

checking1.print_customer_information()
checking2.print_customer_information()