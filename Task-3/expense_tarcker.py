import csv
import os


FILE_NAME = "expenses.csv"


# ==========================================
# CREATE CSV FILE
# ==========================================

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Category",
                "Amount",
                "Description"
            ])


# ==========================================
# ADD EXPENSE
# ==========================================

def add_expense():
    print("\n========== ADD EXPENSE ==========")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            date,
            category,
            amount,
            description
        ])

    print("\nExpense added successfully!")


# ==========================================
# VIEW ALL EXPENSES
# ==========================================

def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        expenses_found = False

        for row in reader:
            expenses_found = True

            print(
                f"Date: {row['Date']} | "
                f"Category: {row['Category']} | "
                f"Amount: ₹{row['Amount']} | "
                f"Description: {row['Description']}"
            )

        if not expenses_found:
            print("No expenses found.")


# ==========================================
# FILTER EXPENSES BY CATEGORY
# ==========================================

def filter_expenses():
    print("\n========== FILTER EXPENSES ==========")

    category = input("Enter category to filter: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            if row["Category"].lower() == category:
                found = True

                print(
                    f"Date: {row['Date']} | "
                    f"Category: {row['Category']} | "
                    f"Amount: ₹{row['Amount']} | "
                    f"Description: {row['Description']}"
                )

        if not found:
            print("No expenses found for this category.")


# ==========================================
# CATEGORY SUMMARY
# ==========================================

def category_summary():
    print("\n========== CATEGORY SUMMARY ==========")

    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No expenses found.")
        return

    total = 0

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")
        total += amount

    print("--------------------------------")
    print(f"Total Expenses: ₹{total:.2f}")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    create_file()

    while True:

        print("\n===================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("===================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please enter 1-5.")


# ==========================================
# START PROGRAM
# ==========================================

main()