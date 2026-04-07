
def main():
    print("\nWelcome to your budget calculator!")

    balance = 0.0 
    transactions = []
    while True:
        print("Pick one of the following options:")
        print("1. Add income")
        print("2. Add expense")
        print("3. View budget")
        print("4. View transactions")
        print("5. Exit")

        choice = input("Enter your choice (1-4):")
        if choice == "1":
            balance = add_income(balance, transactions)
        elif choice == "2":
            balance = add_expense(balance, transactions)
        elif choice == "3":
            view_budget(balance)
        elif choice == "4":
            view_transactions(transactions)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_income(balance, transactions):
    print("\n--- Add Income ---")
    while True:
        amount = float(input("Enter income amount: "))
        balance += amount
        transactions.append(
            {"Income": amount
            }
        )
        print(f"Added income: ${amount:.2f}")

        choice = input("Do you want to add another income? (y/n): ").lower()
        if choice != 'y':
            return balance

def add_expense(balance, transactions):
     print("\n--- Add Expense ---")
     while True:
        amount = float(input("Enter expense amount: "))
        balance -= amount 
        transactions.append(
            {
                "Expense": amount
            }
        )
        print(f"Added expense: ${amount:.2f}")

        choice = input("Do you want to add another expense? (y/n): ").lower()
        if choice != 'y':
            return balance

def view_budget(balance):
    print(f"Current budget: ${balance:.2f}")
    input("Press Enter to return to the main menu...")

def view_transactions(transactions):
    print("\n--- Transaction History ---")
    if not transactions:
        print("No transactions recorded.")
    else:
        for transaction in transactions:
            print(transaction)
    input("Press Enter to return to the main menu...")

main()
