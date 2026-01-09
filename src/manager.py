import json
import os
from expense import Expense

class ExpenseManager:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.expenses = json.load(f)
        else:
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense.to_dict())
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['description']} | {exp['date']}")

    def total_by_category(self):
        summary = {}
        for exp in self.expenses:
            summary[exp['category']] = summary.get(exp['category'], 0) + exp['amount']

        print("\nExpense Summary:")
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")
