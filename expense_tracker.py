import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense saved successfully!")

def view_expenses():
    total = 0
    print("\n--- Expenses ---")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} | {row[1]} | ₹{row[2]}")
                total += float(row[2])
    except FileNotFoundError:
        print("No expenses recorded yet.")

    print("Total Expense:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
