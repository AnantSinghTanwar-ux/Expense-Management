from manager import ExpenseManager

def menu():
    print("\n--- Expense Management System ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

def main():
    manager = ExpenseManager()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            desc = input("Description: ")
            manager.add_expense(amount, category, desc)
            print("✅ Expense added!")

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            manager.total_by_category()

        elif choice == "4":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
