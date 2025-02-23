# src/expense_tracker.py

from src.api_client import APIClient
from datetime import datetime
import argparse

class ExpenseTracker:
    def __init__(self):
        self.api_client = APIClient()

    def add_expense(self, description, amount, date):
        return self.api_client.add_expense(description, amount, date)

    def view_expenses(self):
        return self.api_client.view_expenses()

    def update_expense(self, expense_id, description, amount, date):
        return self.api_client.update_expense(expense_id, description, amount, date)

    def delete_expense(self, expense_id):
        return self.api_client.delete_expense(expense_id)


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():
    tracker = ExpenseTracker()

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add expense command
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("description", help="Description of the expense")
    add_parser.add_argument("amount", type=float, help="Amount of the expense")
    add_parser.add_argument("date", help="Date of the expense in YYYY-MM-DD format")

    # View expenses command
    view_parser = subparsers.add_parser("view", help="View all expenses")

    # Update expense command
    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("id", type=int, help="ID of the expense to update")
    update_parser.add_argument("description", help="New description")
    update_parser.add_argument("amount", type=float, help="New amount")
    update_parser.add_argument("date", help="New date in YYYY-MM-DD format")

    # Delete expense command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("id", type=int, help="ID of the expense to delete")

    args = parser.parse_args()

    # Validate date input for add and update commands
    if args.command in ("add", "update") and not is_valid_date(args.date):
        parser.error("Date must be in YYYY-MM-DD format")

    if args.command == "add":
        response = tracker.add_expense(args.description, args.amount, args.date)
        print("Expense added:", response)
    elif args.command == "view":
        expenses = tracker.view_expenses()
        if expenses:
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. {expense['date']}: {expense['description']} - ${expense['amount']:.2f}")
        else:
            print("No expenses found.")
    elif args.command == "update":
        response = tracker.update_expense(args.id, args.description, args.amount, args.date)
        if response:
            print("Expense updated:", response)
        else:
            print("Update failed. Please check the expense ID.")
    elif args.command == "delete":
        if tracker.delete_expense(args.id):
            print("Expense deleted successfully.")
        else:
            print("Failed to delete expense. Please check the expense ID.")


if __name__ == "__main__":
    main()
