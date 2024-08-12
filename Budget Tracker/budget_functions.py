#This file houses almost all of the functions required to run the main function. 
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime, timedelta
from budget_classes import Income, Expense, Goal
import re

def add_income(incomes, source, hourly_wage, hours_per_week, additional_income):
    """adds the income"""
    incomes.append(Income(source, hourly_wage, hours_per_week, additional_income))

def calculate_income(incomes):
    """calculates the gross and net income of the user"""
    monthly_income = sum(income.hourly_wage * income.hours_per_week * 4 for income in incomes)
    yearly_income = monthly_income * 12
    additional_annual_income = sum(income.additional_income for income in incomes)
    return monthly_income, yearly_income, additional_annual_income

def calculate_taxes(monthly_income):
    """calculates the taxes a person pays based off of federal and utah's tax
      rates to more accuratly calculate the income of the user"""
    tax_rates = {'federal': 22, 'state': 4.95}
    federal_tax_monthly = monthly_income * tax_rates['federal'] / 100
    state_tax_monthly = monthly_income * tax_rates['state'] / 100
    net_monthly = monthly_income - federal_tax_monthly - state_tax_monthly
    return net_monthly, net_monthly * 12

def add_expense(expenses):
    """how a user adds expenses to the trackers"""
    amount = get_float_input("Enter expense amount: ")
    category = input("Enter expense category: ")
    recurring = input("Recurring (Y/N): ").strip().upper()

    if recurring == 'Y' or recurring == 'YES':
        recurrence_type = input("Select type of recurring payment (Monthly, Weekly, Biweekly, Yearly): ").strip().capitalize()
        next_due_date = handle_recurring_dates(recurrence_type)
        date = datetime.now().strftime("%d-%m-%Y")
        expenses.append(Expense(amount, category, date, True, recurrence_type, next_due_date))
    else:
        date = get_valid_date("What day did you pay? (dd-mm-yyyy): ", "%d-%m-%Y")
        expenses.append(Expense(amount, category, date))

def handle_recurring_dates(recurrence_type):
    """if there are any reccuring expenses they are inputed here"""
    if recurrence_type == 'Monthly':
        day = input("What day do you pay? (dd): ")
        return f"{day}-{datetime.now().strftime('%m-%Y')}"
    elif recurrence_type == 'Weekly':
        return (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y")
    elif recurrence_type == 'Biweekly':
        last_payment_date = get_valid_date("When did you last pay? (dd-mm-yyyy): ", "%d-%m-%Y")
        return (last_payment_date + timedelta(days=14)).strftime("%d-%m-%Y")
    elif recurrence_type == 'Yearly':
        day = input("What day do you pay each year? (dd-mm): ")
        return f"{day}-{datetime.now().year}"

def display_expenses_summary(expenses):
    """displays a summary for the expenses"""    
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount
    for category, total in category_totals.items():
        print(f"Total spent on {category}: ${total}")

def add_goal(goals, description, target_amount, target_date):
    """adds a financial goal for the user"""
    goals.append(Goal(description, target_amount, target_date))

def check_goals(goals):
    """used to check the goals already added by the user"""
    for goal in goals:
        print(f"Goal: {goal.description}, Target: ${goal.target_amount} by {goal.target_date.strftime('%d-%m-%Y')}")

def plot_expenses(expenses):
    """creates a graph to show the expenses a person has"""
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount
    categories = list(category_totals.keys())
    totals = list(category_totals.values())
    plt.figure(figsize=(10, 5))
    plt.bar(categories, totals, color='blue')
    plt.xlabel('Category')
    plt.ylabel('Amount Spent')
    plt.title('Expense Distribution')
    plt.show()

def initial_income_setup(incomes):
    """If the user is new this is where they add the details of their income"""
    print("Let's set up your income details.")
    source = input("Enter your primary income source: ")
    hourly_wage = get_float_input("Enter your hourly wage: ")
    hours_per_week = get_float_input("Enter the number of hours you work per week: ")
    additional_income = get_float_input("Enter any additional annual income (e.g., spouse's income): ")
    add_income(incomes, source, hourly_wage, hours_per_week, additional_income)
    return calculate_income(incomes)

def get_valid_date(prompt, date_format):
    """verifys the date the user is inputing is functional with the code"""
    while True:
        date_input = input(prompt)
        try:
            return datetime.strptime(date_input, date_format)
        except ValueError:
            print(f"Invalid date format. Please use {date_format}.")

def get_float_input(prompt):
    """when a user inputs a number it makes sure that it's a valid number"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_expenses(expenses):
    """displays the expenses for the user"""
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nList of all expenses:")
        for index, expense in enumerate(expenses):
            date_str = expense.date.strftime('%d-%m-%Y') if isinstance(expense.date, datetime) else expense.date
            print(f"{index + 1}: {expense.category} - ${expense.amount} on {date_str} (Recurring: {'Yes' if expense.recurring else 'No'})")

def edit_expense(expenses):
    """a function to help a user edit any mistakes or delete any expenses"""
    if not expenses:
        print("No expenses to edit.")
        return

    display_expenses(expenses)
    try:
        expense_number = int(input("Enter the number of the expense you want to edit: ")) - 1
        if 0 <= expense_number < len(expenses):
            expense = expenses[expense_number]
            print("Current details:")
            print(f"{expense_number + 1}: {expense.category} - ${expense.amount} on {expense.date.strftime('%d-%m-%Y')} (Recurring: {expense.recurrence_type if expense.recurring else 'No'})")
            
            # Choosing what to edit
            print("Options: (1) Edit amount, (2) Edit category, (3) Edit date, (4) Edit recurrence, (5) Delete")
            action = input("Choose an action by number: ").strip()

            if action == '1':
                new_amount = get_float_input("Enter new amount: ")
                expense.update_amount(new_amount)
            elif action == '2':
                new_category = input("Enter new category: ")
                expense.update_category(new_category)
            elif action == '3':
                new_date = get_valid_date("Enter new date (DD-MM-YYYY): ", "%d-%m-%Y")
                expense.update_date(new_date)
            elif action == '4':
                new_recurring = input("Is this a recurring expense? (Y/N): ").strip().upper() == 'Y'
                new_recurrence_type = input("Enter new recurrence type (None, Monthly, Weekly, etc.): ") if new_recurring else None
                new_next_due_date = get_valid_date("Enter next due date (DD-MM-YYYY): ", "%d-%m-%Y") if new_recurring else None
                expense.update_recurrence(new_recurring, new_recurrence_type, new_next_due_date)
            elif action == '5':
                expenses.pop(expense_number)
                print("Expense deleted successfully.")
            else:
                print("Invalid action selected. No changes made.")
        else:
            print("Invalid expense number.")
    except ValueError as e:
        print("Error processing your request:", e)

def handle_recurring_dates(recurrence_type):
    """Handles input and returns the next due date for recurring payments based on type."""
    if recurrence_type == 'Monthly':
        day = input("What day do you pay each month? (dd): ")
        return datetime.now().replace(day=int(day)).strftime("%d-%m-%Y")
    elif recurrence_type == 'Weekly':
        return (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y")
    elif recurrence_type == 'Yearly':
        day_month = input("What day and month do you pay each year? (dd-mm): ")
        day, month = map(int, day_month.split('-'))
        return datetime.now().replace(day=day, month=month).strftime("%d-%m-%Y")
    return None

def validate_input(input_type, prompt, pattern=None, range=None):
    """this is a general purpose input validation function. Used to make sure the users don't have the program crash on them. """
    while True:
        user_input = input(prompt).strip()
        if input_type == 'float':
            try:
                value = float(user_input)
                if range and not (range[0] <= value <= range[1]):
                    raise ValueError("Value out of range.")
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif input_type == 'date':
            try:
                parsed_date = datetime.strptime(user_input, pattern)
                if datetime.now() > parsed_date:
                    raise ValueError("Date must be in the future.")
                return parsed_date
            except ValueError:
                print(f"Invalid date format. Please use {pattern}.")
        elif input_type == 'string':
            if pattern and not re.match(pattern, user_input):
                print("Invalid input format.")
            else:
                return user_input