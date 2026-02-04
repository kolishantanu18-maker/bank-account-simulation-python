class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        self.save_transaction(f"Deposited {amount}")
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.save_transaction(f"Withdrawn {amount}")
        print(f"{amount} withdrawn successfully")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def save_transaction(self, message):
        with open("transactions.txt", "a") as file:
            file.write(
                f"Account:{self.acc_no} | {message} | Balance:{self.balance}\n"
            )


def main():
    print("Welcome to Bank Account Simulation")

    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")

    account = BankAccount(acc_no, name)

    while True:
        print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
        """)

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)

            elif choice == "2":
                amt = float(input("Enter withdraw amount: "))
                account.withdraw(amt)

            elif choice == "3":
                account.check_balance()

            elif choice == "4":
                print("Thank you for using banking services")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
