
def main():
    print("\nWelcome to your budget calculator!")
    balance = 0.0 
    while True:
        print("Pick one of the following options:")
        print("1. Add income")
        print("2. Add expense")
        print("3. View budget")
        print("4. Exit")

        choice = input("Enter your choice (1-4):")
        if choice == "1":
            balance = add_income(balance)
        elif choice == "2":
            balance = add_expense(balance)
        elif choice == "3":
            view_budget(balance)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_income(balance):
    print("\n--- Add Income ---")
    while True:
        amount = float(input("Enter income amount: "))
        balance += amount
        print(f"Added income: ${amount:.2f}")

        choice = input("Do you want to add another income? (y/n): ").lower()
        if choice != 'y':
            return balance

def add_expense(balance):
     print("\n--- Add Expense ---")
     while True:
        amount = float(input("Enter expense amount: "))
        balance -= amount 
        print(f"Added expense: ${amount:.2f}")

        choice = input("Do you want to add another expense? (y/n): ").lower()
        if choice != 'y':
            return balance

def view_budget(balance):
    print(f"Current budget: ${balance:.2f}")
    input("Press Enter to return to the main menu...")

main()
