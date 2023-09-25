# CRT-Intern-2
Personal Budget Tracker


The provided code defines a Python class called `BudgetTracker` and a corresponding `main` function to create a simple personal budget tracking system. Here's a description of what each part of the code does:

1. `BudgetTracker` Class:
   - This class is designed to manage a personal budget.
   - Attributes:
     - `balance`: Represents the current balance in the budget.
     - `transactions`: A list to store details of all transactions (deposits and withdrawals).
   - Methods:
     - `_init_(self)`: The constructor initializes the balance as 0 and transactions as an empty list.
     - `deposit(self, amount, description)`: Adds a deposit to the balance and records it in the transactions list.
     - `withdraw(self, amount, description)`: Withdraws an amount if sufficient funds are available and records the withdrawal.
     - `show_balance(self)`: Displays the current balance.
     - `show_transactions(self)`: Prints a list of all transactions with their amounts and descriptions.

2. `main()` Function:
   - This function serves as the main entry point for interacting with the budget tracker.
   - It creates an instance of the `BudgetTracker` class.
   - It runs a loop to display a menu and process user input.
   - Menu options include depositing, withdrawing, showing the balance, showing transaction history, and exiting the program.
   - User input is used to call the corresponding methods of the `BudgetTracker` class.

Overall, this code provides a basic command-line interface for managing personal finances, allowing users to deposit, withdraw, and view their financial transactions. It's a foundation that can be extended and customized to suit more complex budgeting needs.
