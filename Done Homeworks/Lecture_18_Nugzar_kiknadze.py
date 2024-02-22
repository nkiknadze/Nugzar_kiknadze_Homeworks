#Task_N1
'''
შექმენი საბანკო ანგარიშის კლასი, მომხმარებლის, პაროლის და საწყისი თანხის პარამეტრებით. 
თანხის შეტანის, გამოტანის და გადარიცხვის, დარჩენილი ნაშთის ჩვენების მეთოდებით.
__repr__ მეჯიქ მეთოდით.
პაროლის ცვლადი უნდა იყოს private _ ცვლადი და საჭიროა აკმაყოფილებდეს პირობას: მინიმალური სიმბოლოების ოდენობა _ 8.
'''

print("Task_N1")
class BankAccount:
    def __init__(self, username, password, balance):
        self.username = username
        self._password = password
        self.balance = balance

    def show_balance(self):
        return f"Start balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Remaining balance: {self.balance}"

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal {amount}. Remaining balance: {self.balance}"
        else:
            return "Not enough money"

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            return f"Transferred {amount} to {recipient_account.username}. Your remaining balance: {self.balance}"
        else:
            return "Not enough money"

    def __repr__(self):
        return f"BankAccount(username='{self.username}', balance={self.balance})"

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password (minimum 8 characters): ")
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Enter password again: ")

    balance = float(input("Input starting balance: "))
    deposit_amount = float(input("Input deposit amount: "))
    withdrawal_amount = float(input("Input withdrawal amount: "))
    account = BankAccount(username, password, balance)

    print("Result:\n")
    print(account.show_balance())
    print(account.deposit(deposit_amount))
    print(account.withdrawal(withdrawal_amount))
    print(f"{account}\n")

    
