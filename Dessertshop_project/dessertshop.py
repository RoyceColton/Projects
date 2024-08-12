from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt

class DessertShop:
    def __init__(self):
        self.customer_db = {}

    @staticmethod
    def user_prompt_payment_type():
        valid_payment_types = ['CASH', 'CARD', 'PHONE']
        while True:
            payment_type = input("Enter payment type (CASH, CARD, or PHONE): ").upper()
            if payment_type in valid_payment_types:
                return payment_type
            else:
                print("Invalid payment type. Please enter either CASH, CARD, or PHONE.")

    @staticmethod
    def user_prompt_candy():
        name = input("Enter candy name: ")
        price = float(input("Enter candy price: "))
        weight = float(input("Enter candy weight: "))
        return Candy(name, price, weight)

    @staticmethod
    def user_prompt_cookie():
        name = input("Enter cookie name: ")
        quantity = int(input("Enter cookie quantity: "))
        price_per_dozen = float(input("Enter cookie price per dozen: "))
        return Cookie(name, quantity, price_per_dozen)

    @staticmethod
    def user_prompt_icecream():
        name = input("Enter ice cream flavor: ")
        scoops = int(input("Enter number of scoops: "))
        price_per_scoop = float(input("Enter price per scoop: "))
        return IceCream(name, scoops, price_per_scoop)

    @staticmethod
    def user_prompt_sundae():
        base_flavor = input("Enter ice cream flavor for the base: ")
        scoops = int(input("Enter number of scoops: "))
        price_per_scoop = float(input("Enter price per scoop: "))
        topping = input("Enter topping: ")
        topping_price = float(input("Enter topping price: "))
        return Sundae(base_flavor, scoops, price_per_scoop, topping, topping_price)

    @staticmethod
    def user_prompt_customer_name():
        while True:
            customer_name = input("Enter customer's name: ").strip()
            if customer_name:
                return customer_name
            else:
                print("Customer name cannot be empty. Please enter a valid name.")

    def add_customer(self, customer_name, customer):
        if customer_name in self.customer_db:
            print(f"Customer '{customer_name}' already exists! Please enter a different name.")
            return False
        else:
            self.customer_db[customer_name] = customer
            print(f"Customer '{customer_name}' added successfully!")
            return True

    def get_next_customer_id(self):
        return len(self.customer_db) + 1

    def admin_module(self):
        while True:
            print("1: Shop Customer List\n2: Customer Order History\n3: Best Customer\n4: Exit Admin Module")
            choice = input("What would you like to do? (1-4): ")
            
            if choice == '1':
                self.display_customer_list()
            elif choice == '2':
                self.display_customer_order_history()
            elif choice == '3':
                self.display_best_customer()
            elif choice == '4':
                break  # Exit the Admin Module

    def display_customer_list(self):
        print("Customer List:")
        for customer_name, customer in self.customer_db.items():
            print(f"Customer Name: {customer.customer_name}  Customer ID: {customer.customer_id}")

    def display_customer_order_history(self):
        customer_name = input("Enter the name of the customer: ")
        if customer_name in self.customer_db:
            customer = self.customer_db[customer_name]
            print(f"Customer Name: {customer_name}  Customer ID: {customer.customer_id}")
            for index, order in enumerate(customer.order_history):
                print(f"Order #: {index + 1}")
                # Here you would print details about each order
                # This would likely involve iterating over order items and printing them
                # You'll need to implement this part based on how your Order and DessertItem classes are structured

    def display_best_customer(self):
        # Determine the best customer
        max_spent = 0
        best_customer = None
        for customer in self.customer_db.values():
            total_spent = sum(order.total() for order in customer.order_history)  # Assuming an Order.total() method
            if total_spent > max_spent:
                max_spent = total_spent
                best_customer = customer
        if best_customer:
            print(f"The Dessert Shop's most valued customer is: {best_customer.customer_name}!")
        else:
            print("No best customer to display.")

class Customer:
    id_counter = 0  # Initialize the counter at the class level

    def __init__(self, customer_name, order):
        self.customer_name = customer_name
        self.order_history = [order]  # Initialize order history with the provided order
        self.customer_id = self.generate_id()  # Correct method name and generate an ID

    @classmethod
    def generate_id(cls):
        cls.id_counter += 1  # Correctly increment the counter
        return cls.id_counter  # Return the new ID

    @staticmethod
    def add2history(customer_name: str, order: Order) -> "Customer":
        # Create a new Customer object with the provided customer_name and order
        customer = Customer(customer_name, order)
        return customer


def main():
    dessert_shop = DessertShop()

    while True:
        print("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae\n5: Admin Module")
        choice = input("What would you like to add to the order? (1-5, Enter for done): ")

        if choice == '5':
            dessert_shop.admin_module()
            continue
        elif choice in ['1', '2', '3', '4']:
            order = Order()

            prompt_functions = {
                '1': DessertShop.user_prompt_candy,
                '2': DessertShop.user_prompt_cookie,
                '3': DessertShop.user_prompt_icecream,
                '4': DessertShop.user_prompt_sundae
            }

            order.add(prompt_functions[choice]())

            while True:
                add_more = input("Add more items? (y/n): ").lower()
                if add_more == 'n':
                    break
                additional_choice = input("Enter item type (1: Candy, 2: Cookie, 3: Ice Cream, 4: Sundae): ")
                if additional_choice in prompt_functions:
                    order.add(prompt_functions[additional_choice]())

            if len(order) > 0:
                order.sort()
                payment_type = DessertShop.user_prompt_payment_type()
                order.set_pay_type(payment_type)

                customer_name = DessertShop.user_prompt_customer_name()
                customer = Customer(customer_name, order)
                dessert_shop.add_customer(customer_name, customer)

                # Now generate receipt with correct customer details
                data = [["Name", "Cost", "Tax"]]
                for item in order:
                    data.append([item.name, item.calculate_cost(), item.calculate_tax()])
                subtotal = sum(item.calculate_cost() for item in order)
                total_tax = sum(item.calculate_tax() for item in order)
                total_cost = subtotal + total_tax
                total_items = len(order)
                data.append(["Subtotal", subtotal, ""])
                data.append(["Total Tax", total_tax, ""])
                data.append(["Total Cost", total_cost, ""])
                data.append(["Total Items", total_items, ""])

                out_file_name = "receipt.pdf"
                make_receipt(data, payment_type, out_file_name, customer_name, customer.customer_id, len(customer.order_history))

            start_another_order = input("Do you want to start another order? (y/n): ").strip().lower()
            if start_another_order != 'y':
                break
if __name__ == "__main__":
    main()