Simple Command Line Expense Splitter
Overview of the Project

This project is a minimal, single-file Python utility designed to solve the common real-world problem of calculating shared debts after a group event (e.g., a trip, shared groceries, or a weekend outing).

It uses a naive "whack-a-mole" approach to settlement, iteratively transferring money between the first available debtor and the first available creditor until the balances are mostly zeroed out. The code is structured as a non-modular script, mimicking a fast, human-written solution rather than a formal software application.
Features

    User Management: Add any number of participants.

    Expense Logging: Log the description, total amount, and who paid for each expense.

    Equal Splitting: All expenses are currently split equally among all registered users.

    Debt Calculation: Calculates the net balance for every user (who owes whom).

    Naive Settlement: Executes a simple, iterative transfer plan to settle all balances.

    Persistence: Automatically saves and loads all user data and bill history to a local data.json file.

    CSV Export: Optionally exports the final settlement plan to a comma-separated out.csv file.

Technologies/Tools Used

    Language: Python 3.x

    Core Libraries: json, os, sys (Standard Library only)

    Storage: Local JSON file (data.json)

Steps to Install & Run the Project

Since this is a single-file, dependency-free Python script, installation is simple.


    Run the Script: Execute the Python file directly from your terminal:

    python expense_manager.py

Instructions for Use

Once the script is running, follow the simple command prompts:

    Start: The script immediately checks for a data.json file to load previous data.

    Add Users (1): Use option 1 to add all participants one by one (name: John, name: Jane, etc.). You must add all users before adding expenses.

    Add Bills (2): Use option 2 to log an expense. You will be prompted for:

        amt: (The total cost)

        for: (A description, e.g., "Dinner at Joe's")

        payer: (The name of the person who paid the total amount)

    Calculate & Settle (3): Use option 3 to run the settlement logic.

        The script will print the required transfers (e.g., neg_p pays pos_p 12.34).

        It will then ask if you want to export the results to out.csv.

Instructions for Testing

Due to the non-modular, global-state design, unit testing is not easily applied. To test the core functionality, perform the following steps manually:

    Test 1: Simple Equal Split

        Run the script (python expense_manager.py).

        Add users: John, Jane.

        Add a bill: Amount $30.00, Payer John.

        Run settlement (3).

        Expected Result: "Jane pays John 15.0" (The calculation should be $30 / 2 = $15.00).

    Test 2: Multiple Bills

        Keep users John and Jane.

        Add a second bill: Amount $20.00, Payer Jane.

        Run settlement (3).

        Expected Result: John now paid $30, Jane paid $20. Total is $50. Each owes $25. John is net +5, Jane is net −5. Result should be "Jane pays John 5.0".

    Test 3: File Persistence

        After running Test 2, close the script (Ctrl+C or end the process).

        Inspect data.json to ensure John and Jane and the two bills are saved.

        Re-run the script. All data should load automatically.

