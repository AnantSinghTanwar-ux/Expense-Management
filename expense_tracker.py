expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Total Expense")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("Total Expense:", sum(expenses))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
