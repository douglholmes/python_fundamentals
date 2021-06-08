class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self



jane = BankAccount(0.01, 100)
john = BankAccount(0.05, 500)

# user1 make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
# user2 make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)

jane.deposit(10).deposit(10).deposit(10).withdraw(30).yield_interest().display_account_info()

john.deposit(100).deposit(100).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()
