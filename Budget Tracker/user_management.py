#this file tracks the login and signup for the program

import csv
from pathlib import Path

# File path for the CSV file
user_file = Path("users.csv")

def read_users():
    """Read users from a CSV file."""
    users = {}
    if user_file.exists():
        with open(user_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Avoid processing empty rows
                    username, password, role = row
                    users[username] = {'password': password, 'role': role, 'data': {'incomes': [], 'expenses': [], 'goals': []}}
    return users

def write_users(users):
    """Write users to a CSV file."""
    with open(user_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for username, details in users.items():
            writer.writerow([username, details['password'], details['role']])

users = read_users()

def authenticate(username, password):
    """Check if the user exists and the password is correct."""
    if username in users and users[username]['password'] == password:
        return True
    return False

def sign_up(username, password):
    """Register a new user if the username is not already taken."""
    if username in users:
        return False
    else:
        users[username] = {'password': password, 'role': 'user', 'data': {'incomes': [], 'expenses': [], 'goals': []}}
        write_users(users)  # Update the CSV file with the new user
        return True

def get_user_data(username):
    """Retrieve user data from the dictionary."""
    return users.get(username, {}).get('data', {'incomes': [], 'expenses': [], 'goals': []})