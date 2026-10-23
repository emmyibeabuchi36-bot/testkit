# Project 1: Budget Tracker

# Lists to store incomes and expenses
incomes = []
expenses = []


# Function to add income
def add_income():
    name = input("Enter the name of the income: ")
    amount = float(input("Enter the monthly income amount: "))

    incomes.append({
        "name": name,
        "amount": amount
    })

    print("Income added successfully!")


# Function to add expense
def add_expense():
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the monthly expense amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully!")


# Function to view budget summary
def view_budget_summary():
    print("\n========== BUDGET SUMMARY ==========")

    # Display incomes
    print("\nINCOMES:")
    if len(incomes) == 0:
        print("No income has been added.")
    else:
        for income in incomes:
            print(f"- {income['name']}: ₦{income['amount']:.2f}")

    # Display expenses
    print("\nEXPENSES:")
    if len(expenses) == 0:
        print("No expenses have been added.")
    else:
        for expense in expenses:
            print(f"- {expense['name']}: ₦{expense['amount']:.2f}")

    # Calculate totals
    total_income = sum(income["amount"] for income in incomes)
    total_expense = sum(expense["amount"] for expense in expenses)
    net_income = total_income - total_expense

    # Display totals
    print("\n------------------------------------")
    print(f"Total Income:  ₦{total_income:.2f}")
    print(f"Total Expense: ₦{total_expense:.2f}")
    print(f"Net Income:    ₦{net_income:.2f}")
    print("====================================")


# Main program
while True:
    print("\n========== BUDGET TRACKER ==========")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget Summary")
    print("4. Exit")
    print("====================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_budget_summary()

    elif choice == "4":
        print("Thank you for using the Budget Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 4.")
