class BankAccount:
    def __init__(self, account_number, balance=0):
        # private attributes (name mangling)
        self.__account_number = account_number
        self.__balance = balance

    # Getter account_number (read-only property)
    @property
    def account_number(self):
        return f"XXXX-XXXX-{str(self.__account_number)[-4:]}"  # masked for security

    # Getter for balance
    @property
    def balance(self):
        return self.__balance

    # Setter for balance (with encapsulated validation)
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        print(f"Balance updated: {self.__balance} → {amount}")
        self.__balance = amount

    # Public method for deposit
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.__balance += amount
        print(f"Deposited {amount}, new balance: {self.__balance}")

    # Public method for withdraw
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        print(f"Withdrew {amount}, new balance: {self.__balance}")

    # Static method belongs to the class, not instance
    @staticmethod
    def bank_policy():
        return "All accounts must maintain a minimum balance of $100."


# Usage
acc = BankAccount("123456789012", 1000)

print("Account Number:", acc.account_number)  # Encapsulation: only masked version
print("Balance:", acc.balance)  # Controlled access

acc.deposit(500)
acc.withdraw(300)

# Direct assignment goes through encapsulated validation
acc.balance = 2000

# Static method call without instance
print("Policy:", BankAccount.bank_policy())

# Trying to bypass encapsulation (not recommended)
print(acc._BankAccount__balance)  # Name mangling allows access, but not intended
