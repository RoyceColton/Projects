from datetime import datetime
import msvcrt  # For Windows keyboard input
from user_management import authenticate, sign_up, get_user_data
from budget_functions import (add_income, calculate_income, calculate_taxes,
                              add_expense, display_expenses_summary, add_goal,
                              check_goals, plot_expenses, initial_income_setup,
                              display_expenses, edit_expense, get_float_input, get_valid_date, validate_input)

def main():
    """Main script for the budget tracker application"""
    print("Hi, welcome to Royce's family-friendly budget tracker!")
    new_user = False
    while True:
        user_input = validate_input('string', "Do you want to login or signup? (login/signup): ", pattern='^(login|signup)$').lower()
        
        username = input("Username: ")
        password = input("Password: ")

        if user_input == 'login':
            if authenticate(username, password):
                print("Login successful.")
                break
            else:
                print("Invalid username or password. Please try again.")
        elif user_input == 'signup':
            if sign_up(username, password):
                print("Signup successful.")
                new_user = True
                break
            else:
                print("Username already exists. Please try another one.")

    data = get_user_data(username)
    incomes, expenses, goals = data['incomes'], data['expenses'], data['goals']

    if new_user:
        """If there is a new user this section adds them and asks basic questions about their income so they can see the income to 
        expense ratios and adjust their budget as needed"""
        monthly_income, yearly_income, additional_annual_income = initial_income_setup(incomes)
        print(f"Your monthly gross income is ${monthly_income}, and your yearly gross income is ${yearly_income}.")
        print(f"Additional yearly income is ${additional_annual_income}")
        net_monthly, net_yearly = calculate_taxes(monthly_income)
        print(f"Your monthly net income is ${net_monthly}, and your yearly net income is ${net_yearly}")

    options = {
        '1': {'label': 'Add Expense', 'action': lambda: add_expense(expenses)},
        '2': {'label': 'Add Financial Goal', 'action': lambda: add_goal_interface(goals)},
        '3': {'label': 'Check Financial Goals and Expense Graph', 'action': lambda: check_goals_and_plot(goals, expenses)},
        '4': {'label': 'View All Expenses', 'action': lambda: display_expenses(expenses)},
        '5': {'label': 'Edit an Expense', 'action': lambda: edit_expense(expenses)},
        '6': {'label': 'Logout', 'action': lambda: exit()}
    }
    while True:
        print("\nMenu:")
        for key, option in options.items():
            print(f"{key}. {option['label']}")
        choice = get_choice(options)
        if choice in options:
            options[choice]['action']()  # Make sure you're calling the function correctly
        else:
            print("Invalid choice. Please try again.")

def get_choice(options):
    """Get user input for menu choices"""
    print("Enter your choice:")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key in options:
                return key
            else:
                print("Invalid choice. Please try again.")

def add_goal_interface(goals):
    """Interface to add financial goals"""
    try:
        description = input("Enter goal description: ")
        target_amount = get_float_input("Enter target amount: ")
        target_date = get_valid_date("Enter target date (DD-MM-YYYY): ", "%d-%m-%Y")
        add_goal(goals, description, target_amount, target_date)
        print("Goal added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the goal: {e}")

def check_goals_and_plot(goals, expenses):
    """Check financial goals and plot expenses graph."""
    check_goals(goals)
    plot_expenses(expenses)

if __name__ == "__main__":
    main()