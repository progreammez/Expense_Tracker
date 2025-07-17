print("Welcome to my expense tracker!")

expenses = {
    'January': {
        'Week_1': {'Groceries': 1200, 'Fuel': 900, 'Misc': 300},
        'Week_2': {'Groceries': 600, 'Fuel': 100, 'Misc': 900},
        'Week_3': {'Groceries': 900, 'Fuel': 1300, 'Misc': 1000},
        'Week_4': {'Groceries': 500, 'Fuel': 1000, 'Misc': 100},
    },
    'February': {
        'Week_1': {'Groceries': 600, 'Fuel': 100, 'Misc': 300},
        'Week_2': {'Groceries': 500, 'Fuel': 500, 'Misc': 100},
        'Week_3': {'Groceries': 950, 'Fuel': 1500, 'Misc': 400},
        'Week_4': {'Groceries': 760, 'Fuel': 1300, 'Misc': 700},
    },
    'March' : {
        'Week_1': {'Groceries': 850, 'Fuel': 2000, 'Misc': 500},
        'Week_2': {'Groceries': 300, 'Fuel': 900, 'Misc': 100},
        'Week_3': {'Groceries': 670, 'Fuel': 1900, 'Misc': 350},
        'Week_4': {'Groceries': 500, 'Fuel': 600, 'Misc': 300},
    }
}

while True:
    print("""
What would you like to do today?
1. Add an expense
2. Update a previous expense
3. Delete a previous expense
4. View past expenses
5. Exit
""")
    choice = int(input())
    
    #AddingExpense
    if choice == 1:
        add_month = input("Which month does this expense belong?: ").capitalize()
        add_week = input("Which week does this expense belong to?(Week_1/Week_2/...): ").capitalize()
        add_expense_category = input("Add the category of the expense: ").capitalize()
        add_expense_amount = int(input("Add the expense amount: "))
        
        #DopeLogic(TTR)
        if add_month not in expenses:
            expenses[add_month] = {}
        if add_week not in expenses[add_month]:
            expenses[add_month][add_week] = {}
        if add_expense_category in expenses[add_month][add_week]:
            expenses[add_month][add_week][add_expense_category] += add_expense_amount
        else:
            expenses[add_month][add_week][add_expense_category] = add_expense_amount

        print("Expense added succesfully!")

    #UpdatingExpense
    elif choice == 2:
        update_month = input("Enter the month's expense you want to update: ").capitalize()
        if update_month in expenses:
            update_week = input("Enter the week's expense you want to update(Week_1/Week_2/...): ").capitalize()
            if update_week in expenses[update_month]:
                update_expense_category = input("Enter the category you want to update: ").capitalize()
                if update_expense_category in expenses[update_month][update_week]:
                    update_expense_amount = int(input("Update the expense amount: "))
                    expenses[update_month][update_week][update_expense_category] = update_expense_amount
                    print("Expense added successfully")
                else:
                    print("Record not found")
            else:
                print("Record not found")
        else:
            print("Record not found") 

    #DeletingExpense
    elif choice == 3:
        delete_month = input("Enter the month's expense you want to delete: ").capitalize()
        if delete_month in expenses:
            delete_week = input("Enter the week's expense you want to delete(Week_1/Week_2/...): ").capitalize()
            if delete_week in expenses[delete_month]:
                delete_expense_category = input("Enter the category you want to delete: ").capitalize()
                if delete_expense_category in expenses[delete_month][delete_week]:
                    del expenses[delete_month][delete_week][delete_expense_category]
                    print("Expense successfully deleted.")
                    if not expenses[delete_month][delete_week]:
                        del expenses[delete_month][delete_week]
                        print("Week deleted as there were no categories left.")
                    if not expenses[delete_month]:
                        del expenses[delete_month]
                        print("Month deleted as there were no weeks left.")
                else:
                    print("Record not found.")
            else:
                print("Record not found.")
        else:
            print("Record not found.")

    #ViewingExpense
    elif choice == 4:
        print("""
What do you want to view?
1. All the expenses.
2. A particular month's expense.
3. A particular week's expense.
""")
        view_choice = int(input())
        if view_choice == 1:
            for month, weeks in expenses.items():
                print(f"\n{month} : ")
                for week,categories in weeks.items():
                    print(f" {week} : ")
                    for cat,amt in categories.items():
                        print(f"--> {cat} : {amt}")
        elif view_choice == 2:
            view_month = input("Enter the month's expense you want to view: ").capitalize()
            if view_month in expenses:
                for week,categories in expenses[view_month].items():
                    print(f"{week} : ")
                    for cat,amt in categories.items():
                        print(f"--> {cat} : {amt}")
        elif view_choice == 3:
            view_month = input("Enter the month: ").capitalize()
            if view_month in expenses:
                view_week = input("Enter the week's expense you want to view: ").capitalize()
                if view_week in expenses[view_month]:
                    print(f"Expenses of {view_month}'s {view_week}")
                    for cat,amt in expenses[view_month][view_week].items():
                        print(f"--> {cat} : {amt}")
                else:
                    print("Week not found.")
            else:
                print("Month not found.")
        else:
            print("Invalid response.")

    #Exit
    elif choice == 5:
        print("Exiting expense tracker.")
        break

    #Invalid
    else:
        print("Enter valid response.")
