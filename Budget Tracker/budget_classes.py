#This file houses all of the classes for the budget tracker. 
from datetime import datetime

class Income:
    def __init__(self, source, hourly_wage, hours_per_week, additional_income=0):
        self.source = source
        self.hourly_wage = hourly_wage
        self.hours_per_week = hours_per_week
        self.additional_income = additional_income

    def annual_income(self):
        return self.hourly_wage * self.hours_per_week * 52 + self.additional_income


from datetime import datetime

class Expense:
    def __init__(self, amount, category, date, recurring=False, recurrence_type=None, next_due_date=None):
        self.amount = amount
        self.category = category
        self.date = self.ensure_datetime(date)
        self.recurring = recurring
        self.recurrence_type = recurrence_type
        self.next_due_date = self.ensure_datetime(next_due_date) if next_due_date else None

    def update_amount(self, new_amount):
        """Update the expense amount."""
        self.amount = new_amount
        print(f"Updated amount to ${new_amount}")

    def update_category(self, new_category):
        """Update the expense category."""
        self.category = new_category
        print(f"Updated category to {new_category}")

    def update_date(self, new_date):
        """Update the date of the expense."""
        self.date = self.ensure_datetime(new_date)
        print(f"Updated date to {self.date.strftime('%d-%m-%Y')}")

    def update_recurrence(self, new_recurring, new_recurrence_type=None, new_next_due_date=None):
        """Update the recurrence settings for the expense."""
        self.recurring = new_recurring
        self.recurrence_type = new_recurrence_type
        self.next_due_date = self.ensure_datetime(new_next_due_date) if new_next_due_date else None
        if new_recurring:
            next_due_str = self.next_due_date.strftime('%d-%m-%Y') if self.next_due_date else "N/A"
            print(f"Updated to recurring: {new_recurrence_type}, next due on {next_due_str}")
        else:
            print("Updated to not recurring.")

    @staticmethod
    def ensure_datetime(date):
        """Ensure the provided date is a datetime object."""
        if isinstance(date, datetime):
            return date
        try:
            return datetime.strptime(date, '%d-%m-%Y')
        except TypeError:
            raise ValueError("Invalid date format. Dates must be datetime objects or strings in DD-MM-YYYY format.")



class Goal:
    def __init__(self, description, target_amount, target_date):
        self.description = description
        self.target_amount = target_amount
        if isinstance(target_date, datetime):
            self.target_date = target_date
        else:
            try:
                self.target_date = datetime.strptime(target_date, "%d-%m-%Y")
            except ValueError as e:
                print(f"Error parsing target date: {target_date}. Please ensure the date is in DD-MM-YYYY format.")
                raise e
