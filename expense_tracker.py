from datetime import datetime

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = datetime.now().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        total = 0
        print("\n--- Expenses ---")
        for e in expenses:
            print(f"{e['date']} | {e['category']} | ₹{e['amount']}")
            total += e["amount"]

        print("Total Expense:", total)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option")
