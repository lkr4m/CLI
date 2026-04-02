
def main():
    while True:
        print("Welcome to your budget calculator!")
        print("Pick one of the following options:")
        print("1. Add income")
        print("2. Add expense")
        print("3. View budget")
        print("4. Exit")

        choice = input("Enter your choice (1-4):")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_budget()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_income():
    while True:
        amount = float(input("Enter income amount: "))
        print(f"Added income: ${amount:.2f}")

        choice = input("Do you want to add another income? (y/n): ").lower()
        if choice != 'y':
            break

def add_expense():
    while True:
        amount = float(input("Enter expense amount: "))
        print(f"Added expense: ${amount:.2f}")

        choice = input("Do you want to add another expense? (y/n): ").lower()
        if choice != 'y':
            break

def view_budget():
    print("Viewing budget...")

main()
