# 💸 CLI Expense Tracker

Welcome to my **Command-Line Expense Tracker** — a Python-based project to help you track your weekly and monthly expenses in a clean and structured way.

---

## 🚀 Features

- 🔹 Add new expenses by month, week, and category (Groceries, Fuel, Misc)
- 📝 Update previously entered expense data
- 🗑️ Delete specific categories, weeks, or entire months (auto cleanup enabled)
- 👁️ View options:
  - All expenses at once
  - Specific month's expense breakdown
  - Specific week of a specific month
- 🧠 Smart handling of invalid inputs
- 📦 Clean nested dictionary structure (no empty keys)

---

## 📂 How It Works

This is a Python CLI app that uses nested dictionaries to store and manage expenses:

```python
expenses = {
    'January': {
        'Week_1': {'Groceries': 500, 'Fuel': 1000, 'Misc': 300},
        'Week_2': {...}
    },
    'February': {
        'Week_1': {...}
    }
}
```
Every function — add, update, delete, and view — navigates this structure dynamically, with clean input checks and fallbacks.

## 🖥️ Usage
Clone the repo or download the .py file

Run the script in terminal:

python expense_tracker.py
Follow the prompts and enjoy the vibes 🧾✅

## 📸 Sample Output

Welcome to my expense tracker!

What would you like to do today?
1. Add an expense
2. Update a previous expense
3. Delete a previous expense
4. View past expenses
5. Exit
You’ll be prompted to input the month, week (Week_1, Week_2, ...), category, and amount.

## 💡 Future Plans
💾 Save and load data to/from JSON files (persistence)

📊 Visual dashboard with charts using matplotlib

📱 GUI version with tkinter or a Flask-based web app

✅ Add monthly/weekly total summaries

## 🤝 Contributing
This is a solo project for learning, but if you got ideas, hit me up or fork it. I'm always open to collaborating on cool stuff.
