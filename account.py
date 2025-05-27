class Account:
    def __init__(self, name):
        self.name = name
        self.deposit_list = []
        self.withdraw_list = []
        self.loan = 0
        self.balance = 0
        self.transaction = []
        self.is_secure = True
        self.mini_balance = 58
    def getbalance(self):
        sum_withdraw = sum(self.withdraw_list)
        sum_deposit = sum(self.deposit_list)
        self.balance = sum_deposit - sum_withdraw
        return f"Dear {self.name}, your current balance is {self.balance}"
    def deposit(self, amount):
        if amount > 0:
            self.deposit_list.append(amount)
            self.transaction.append(f"Deposited {amount}")
            return self.getbalance()
        else:
            return "Please deposit a positive amount"
    def withdraw(self, amount):
        self.getbalance()
        if (self.balance - amount) >= self.mini_balance:
            self.withdraw_list.append(amount)
            self.transaction.append(f"Withdrew {amount}")
            return self.getbalance()
        else:
            return "Insufficient funds or minimum balance requirement not met"
    def transfer(self, person, amount):
        self.getbalance()
        if isinstance(person, Account):
            if self.balance - amount >= self.mini_balance:
                person.deposit_list.append(amount)
                self.withdraw_list.append(amount)
                message = f"Dear {self.name}, you transferred {amount} to {person.name}"
                self.transaction.append(message)
                return message
            else:
                return "Insufficient funds for transfer"
        else:
            return "Invalid account details. Please check the account"
    def request_loan(self, loan):
        self.getbalance()
        if loan <= (self.balance * 3):
            self.loan = loan
            self.balance += loan
            self.transaction.append(f"Loan requested: {loan}")
            return f"You're approved. New balance is {self.balance}"
        else:
            return "You're not eligible for this loan"
    def repay_loan(self, amount):
        if self.loan > 0:
            if amount < self.loan:
                self.loan -= amount
                self.balance -= amount
                self.transaction.append(f"Loan repayment of {amount}")
                return f"Remaining loan to pay{self.loan}, balance is now {self.balance}"
            elif amount == self.loan:
                self.balance -= amount
                self.loan = 0
                self.transaction.append(f"Loan fully repaid with {amount}")
                return "Loan fully repaid!"
            else:
                change = amount - self.loan
                self.balance -= self.loan
                self.transaction.append(f"Loan fully repaid. Extra {change} returned")
                self.loan = 0
                return f"Loan repaid. Your change is {change}"
        else:
            return "You have no loan to repay"
    def account_details(self):
        return f"Name: {self.name}, {self.getbalance()}"
    def change_account_name(self, newname):
        oldname = self.name
        self.name = newname
        return f"You successfully changed your name from {oldname} to {newname}"
    def account_statement(self):
        if self.transaction:
            for action in self.transaction:
                print(action)
        else:
            print("No transactions yet")
    def calculate_interest(self):
        self.getbalance()
        interest = self.balance * 0.05
        self.balance += interest
        self.transaction.append(f"Interest added: {interest}")
        return f"Interest of {interest} added. New balance is {self.balance}"
    def freeze(self):
        if not self.is_secure:
            self.is_freeze = True
            return "Your account has been frozen for security"
        else:
            self.is_freeze = False
            return "Your account is safe and unfrozen"
    def unfreeze(self):
        if self.is_freeze:
            self.is_freeze = False
            return "Your account is now active"
        else:
            return "Account was already active"
    def minimum_balance(self):
        return f"Your balance must always be at least {self.mini_balance} after withdrawal"
    def close_balance(self):
        self.balance = 0
        self.transaction.clear()
        self.deposit_list.clear()
        self.withdraw_list.clear()
        self.loan = 0
        return "Account closed and all data cleared"