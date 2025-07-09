# Wisdom Bank Project: 

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}$ deposited successfully.")
        else:
            print("Invalid deposit amount! Please Enter the amount more than zero !")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount}$ withdrawn successfully.")
        else:
            print("Not enough Money!")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


def main():
    print("🙏 Welcome to Wisdom Bank!🏦")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nChoose an option:\n 1. Deposit Amount \t 2. Withdraw Amount \t 3. Check Bank Balance \t 4. Exit \n")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input(f"Enter amount to deposit: $"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("🙏 Thank you for using Wisdom Bank!💵")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
