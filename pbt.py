class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount, description):
        self.balance += amount
        self.transactions.append((amount, description, 'Deposit'))

    def withdraw(self, amount, description):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append((amount, description, 'Withdrawal'))
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")

    def show_transactions(self):
        for trans in self.transactions:
            amount, description, trans_type = trans
            print(f"{trans_type}: ${amount} - {description}")

def main():
    budget = BudgetTracker()
    
    while True:
        print("\nPersonal Budget Tracker Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Show Transactions")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            description = input("Enter a description: ")
            budget.deposit(amount, description)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            description = input("Enter a description: ")
            budget.withdraw(amount, description)
        elif choice == '3':
            budget.show_balance()
        elif choice == '4':
            budget.show_transactions()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
