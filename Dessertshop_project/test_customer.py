import pytest
from dessertshop import Customer

def test_customer_attributes():
    # Create a Customer object
    customer_name = "John Doe"
    order = "Sample Order"
    customer = Customer(customer_name, order)

    # Test customer_name attribute
    assert customer.customer_name == customer_name

    # Test order_history attribute
    assert customer.order_history == [order]

    # Test customer_id attribute (assuming it's initialized to None)
    assert customer.customer_id is None

def test_unique_customer_ids():
    # Create multiple Customer objects
    customer_names = ["Alice", "Bob", "Charlie"]
    orders = ["Order 1", "Order 2", "Order 3"]
    customer_ids = set()

    for name, order in zip(customer_names, orders):
        customer = Customer(name, order)
        customer_ids.add(customer.customer_id)

    # Ensure customer IDs are unique
    assert len(customer_ids) == len(customer_names)