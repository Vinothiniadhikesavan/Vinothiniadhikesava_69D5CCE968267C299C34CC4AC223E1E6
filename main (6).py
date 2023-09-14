class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__account_balance}."
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}"

if __name__ == "__main__":
    my_account = BankAccount("12345", "John Doe", 1000)
    print(my_account.display_balance())  
print(my_account.deposit(500))  
print(my_account.withdraw(200))   
print(my_account.withdraw(1500))   
print(my_account.display_balance())  
