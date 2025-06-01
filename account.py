from datetime import datetime
class Transaction:
    def __init__(self,narration, amount, transaction_type ):
        self.date_time=datetime.now()
        self.narration=narration
        self.amount=amount
        self.transction_type=transaction_type
    def __str__(self):
        return f"{self.date_time}_{self.narration}:{self.amount}({self.transction_type})"
class Account:
    def __init__(self, name,account_number):
        self.name = name
        self.__account_number=account_number
        self.__loan = 0
        self.__balance = 0
        self.transaction = []
        self.is_secure = True
        self.is_freeze=False
        self.__mini_balance = 58
    def getbalance(self):
        return f"Dear {self.name}, your current balance is {self.__balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
            self.transaction.append(Transaction("Deposit",amount,"credit"))
            return self.getbalance()
        else:
            return "Deposit must be positive."
    def withdraw(self, amount):
        self.getbalance()
        if (self.__balance - amount) >= self.__mini_balance:
            self.__balance-=amount
            self.transaction.append(Transaction("Withdrawal",amount,"debit"))
            return self.getbalance()
        else:
            return "Insufficient funds or minimum balance requirement not met"
    def transfer(self, recipient, amount):
        if isinstance(recipient, Account):
            if self.__balance - amount >= self.__mini_balance:
                self.__balance-=amount
                recipient.__balance+=amount
                self.transaction.append(Transaction(f"Transfer to {recipient.name}",amount,"credit"))
                recipient.transaction.append(Transaction(f"Transfer from {self.name}",amount,"credit"))
                return f"Transferred{amount} to {recipient.name}"
            else:

                return "Insufficient funds for transfer"
        else:
            return "Invalid account details. Please check the account"
    def request_loan(self, loan):
        if loan <= (self.__balance * 3):
            self.__loan = loan
            self.__balance += loan
            self.transaction.append(Transaction("Loan credited",loan,"credit"))
            return f"Loan approved. Your balance is {self.__balance}"
        else:
            return "You're not eligible for this loan"
    def repay_loan(self, amount):
        if self.__loan > 0:
            if amount < self.__loan:
                self.__loan -= amount
                self.__balance -= amount
                self.transaction.append(Transaction("Loan repayment",amount,"debit"))
                return f"Remaining loan to pay{self.__loan}, balance is now {self.__balance}"
            elif amount == self.__loan:
                self.__balance -= amount
                self.__loan = 0
                self.transaction.append(Transaction("LOne repayment",amount,"debit"))
                return "Loan fully repaid!"
            else:
                change = amount - self.__loan
                self.__balance -= self.__loan
                self.transaction.append(Transaction("Loan fully repaid",self.__loan,"debit"))
                self.__loan = 0
                return f"Loan repaid.Extra change is {change}"
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
        interest = self.__balance * 0.05
        self.__balance += interest
        self.transaction.append(Transaction("Interest added",interest,"credit"))
        return f"Interest of {interest} added. New balance is {self.__balance}"
    def freeze(self):
        if not self.is_secure and not self.is_freeze:
            self.is_freeze = True
            return "Your account has been frozen for security reasons"
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
        return f"Your balance must always be at least {self.__mini_balance} after withdrawal"
    def close_balance(self):
        self.__balance = 0
        self.transaction.clear()
        self.__loan = 0
        return "Account closed and all data cleared"
account = Account("Meron","AC1000")
account2 = Account("Ruta","Ac1002")
print(account.deposit(300))
print(account.withdraw(30))
print(account.transfer(account2,50))
print(account.request_loan(200))
print(account.repay_loan(30))
print(account.repay_loan(200))
print(account.calculate_interest())
account.account_statement()



    



    
    