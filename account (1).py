import datetime

class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: ${amount}"

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Current Balance: ${self.balance}")


# Example usage:
account = BankAccount(account_number="25803699", balance=1000, customer_name="Morgan Hakim")

print(account.deposit(500))
print(account.withdraw(200))
account.check_balance()
account.customer_details()
