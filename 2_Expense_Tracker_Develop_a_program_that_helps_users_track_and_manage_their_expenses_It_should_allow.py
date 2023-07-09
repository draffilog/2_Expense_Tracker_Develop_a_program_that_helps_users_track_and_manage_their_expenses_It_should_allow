import matplotlib.pyplot as plt

expenses = {}

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))

    if date not in expenses:
        expenses[date] = {}

    if category not in expenses[date]:
        expenses[date][category] = amount
    else:
        expenses[date][category] += amount

    print("Expense added successfully!")

def generate_report():
    total_spending = 0
    for date in expenses:
        print("Date:", date)
        for category, amount in expenses[date].items():
            print("Category:", category)
            print("Amount:", amount)
            total_spending += amount
        print("--------------------")
    print("Total Spending:", total_spending)

def generate_graph():
    categories = []
    amounts = []

    for date in expenses:
        for category, amount in expenses[date].items():
            if category not in categories:
                categories.append(category)
                amounts.append(amount)
            else:
                index = categories.index(category)
                amounts[index] += amount

    plt.bar(categories, amounts)
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.title("Expense Tracker")
    plt.show()

def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. Generate Report")
        print("3. Generate Graph")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            generate_graph()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()