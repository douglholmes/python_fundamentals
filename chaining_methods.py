class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def diplay_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    #bonus assignment that I was working to figure out
    # def transfer_money(self, other_user , amount):
    #     other_user.make_deposit(amount)
    #     self.make_withdrawal(amount)
        


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
john = User("John Smith", "johnsmith@aol.com")
#first user
guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(25).diplay_user_balance()
#second user
monty.make_deposit(500).make_deposit(100).make_withdrawal(50).make_withdrawal(100).diplay_user_balance()
#third user
john.make_deposit(900).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).diplay_user_balance()