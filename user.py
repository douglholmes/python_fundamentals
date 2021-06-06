class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
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
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(25)
guido.diplay_user_balance()
guido.transfer_money(john,100)
#second user
monty.make_deposit(500)
monty.make_deposit(100)
monty.make_withdrawal(50)
monty.make_withdrawal(100)
monty.diplay_user_balance()

#third user
john.make_deposit(900)
john.make_withdrawal(100)
john.make_withdrawal(100)
john.make_withdrawal(100)
john.diplay_user_balance()