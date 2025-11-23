import os

# Global lists to store data in memory
users = []
expenses = []
FILE_NAME = "expense_data.txt"

def load_data():
    """Reads data from a simple text file without using JSON."""
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            
            # Section 1: Read Users (First line starts with USERS:)
            if len(lines) > 0 and lines[0].startswith("USERS:"):
                user_line = lines[0].replace("USERS:", "").strip()
                if user_line:
                    global users
                    users = user_line.split(",")

            # Section 2: Read Expenses (Remaining lines)
            for i in range(1, len(lines)):
                parts = lines[i].strip().split("|")
                if len(parts) == 3:
                    # Format: Payer|Amount|Description
                    exp = {
                        "payer": parts[0],
                        "amount": float(parts[1]),
                        "desc": parts[2]
                    }
                    expenses.append(exp)
        print(">> Data loaded successfully.")
    except Exception as e:
        print("Error loading file:", e)

def save_data():
    """Saves data to a text file using simple string formatting."""
    try:
        with open(FILE_NAME, "w") as f:
            # Save Users on the first line
            user_str = "USERS:" + ",".join(users) + "\n"
            f.write(user_str)

            # Save Expenses on subsequent lines
            for exp in expenses:
                line = f"{exp['payer']}|{exp['amount']}|{exp['desc']}\n"
                f.write(line)
        print(">> Data saved to", FILE_NAME)
    except Exception as e:
        print("Error saving data:", e)

def add_user():
    print("\n--- ADD NEW USER ---")
    name = input("Enter name: ").strip().title()
    if name in users:
        print("Error: User already exists.")
    elif name == "":
        print("Error: Name cannot be empty.")
    else:
        users.append(name)
        print(f"User '{name}' added.")
        save_data()

def add_expense():
    print("\n--- ADD NEW EXPENSE ---")
    if not users:
        print("Error: No users found. Add users first.")
        return

    print("Current Users:", ", ".join(users))
    payer = input("Who paid? ").strip().title()
    
    if payer not in users:
        print("Error: That person is not in the user list.")
        return

    try:
        amount = float(input("Enter amount: "))
        desc = input("What was it for? (e.g. Lunch): ")
        
        new_expense = {
            "payer": payer,
            "amount": amount,
            "desc": desc
        }
        expenses.append(new_expense)
        print("Expense recorded.")
        save_data()
    except ValueError:
        print("Error: Amount must be a number.")

def calculate_split():
    print("\n--- SETTLING DEBTS ---")
    if not users or not expenses:
        print("Nothing to calculate yet.")
        return

    # 1. Calculate Total Spent per person
    total_spent = 0
    paid_by_person = {u: 0.0 for u in users}

    for exp in expenses:
        paid_by_person[exp['payer']] += exp['amount']
        total_spent += exp['amount']

    # 2. Calculate Fair Share
    fair_share = total_spent / len(users)
    print(f"Total Spent: {total_spent:.2f}")
    print(f"Share per person: {fair_share:.2f}\n")

    # 3. Calculate Net Balance (Positive = Owed money, Negative = Owes money)
    balances = {}
    for u in users:
        balances[u] = paid_by_person[u] - fair_share

    # 4. Separate into Debtors (owe money) and Creditors (receive money)
    debtors = []
    creditors = []

    for name, amount in balances.items():
        if amount < -0.01: # Small threshold for float errors
            debtors.append({"name": name, "amt": amount})
        elif amount > 0.01:
            creditors.append({"name": name, "amt": amount})

    # 5. Settlement Algorithm (Greedy approach)
    print("--- Transactions Required ---")
    
    # Sort to optimize transactions (optional, but looks cleaner)
    debtors.sort(key=lambda x: x['amt'])
    creditors.sort(key=lambda x: x['amt'], reverse=True)

    d_index = 0
    c_index = 0

    while d_index < len(debtors) and c_index < len(creditors):
        debtor = debtors[d_index]
        creditor = creditors[c_index]

        # The amount to settle is the minimum of what is owed vs what is due
        amount = min(abs(debtor['amt']), creditor['amt'])

        print(f"{debtor['name']} pays {creditor['name']}: {amount:.2f}")

        # Adjust balances
        debtor['amt'] += amount
        creditor['amt'] -= amount

        # Move to next person if their balance is settled (close to 0)
        if abs(debtor['amt']) < 0.01:
            d_index += 1
        if creditor['amt'] < 0.01:
            c_index += 1

def main_menu():
    load_data() # Load old data on startup
    while True:
        print("\n=== EXPENSE SPLITTER ===")
        print("1. Add User")
        print("2. Add Expense")
        print("3. Calculate & Settle")
        print("4. Exit")
        
        choice = input("Select option (1-4): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            calculate_split()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
