# Project Statement

## Introduction
This project implements a simple command-line Expense Splitter that allows users to add participants, record expenses, and automatically calculate how much each person owes or is owed. The program is designed to be lightweight, dependency-free, and easy to run on any machine with Python installed.

## Problem Statement
Managing shared expenses in group situations is often confusing and error-prone. People forget who paid, totals become inconsistent, and settling accounts becomes difficult. The problem is to build a minimal tool that can accurately record expenses and compute a fair settlement without relying on complex applications.

## Objectives
- Allow users to add participants.
- Record expenses with payer, amount, and description.
- Automatically calculate the fair share for each user.
- Determine who owes money and generate settlement transactions.
- Maintain persistent data using a simple text-based file.

## Scope of the Project
The project covers user management, expense logging, settlement calculation, and simple text-file storage. It does not include GUI development, advanced database systems, or multi-group support.

## Project Deliverables
- A Python script implementing the Expense Splitter.
- Persistent storage through `expense_data.txt`.
- A functioning command-line menu system.
- Settlement output that clearly lists required payments.
- Project documentation and report.

## Methodology Overview
1. Load existing data from the text file.
2. Allow users to add members and log expenses.
3. Use a greedy algorithm to settle balances.
4. Save all updates back to the file.
5. Display results directly in the terminal.

## Expected Outcome
A working, easy-to-use CLI program that simplifies shared expense management and produces accurate settlement instructions.

## Tools & Technologies Used
- **Language:** Python
- **Storage:** Plain text file
- **Execution:** Terminal / Command Line

## Conclusion
The project successfully demonstrates modular programming, file handling, and algorithmic settlement logic. It provides a practical utility while maintaining simplicity and portability.
