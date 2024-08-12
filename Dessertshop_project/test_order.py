import pytest
from dessert import Order, Candy

@pytest.fixture
def order():
    return Order()

def test_valid_payment_types(order):
    # Test setting valid payment types
    order.set_pay_type('CASH')
    assert order.get_pay_type() == 'CASH'

    order.set_pay_type('CARD')
    assert order.get_pay_type() == 'CARD'

    order.set_pay_type('PHONE')
    assert order.get_pay_type() == 'PHONE'

def test_invalid_payment_type(order):
    # Test setting invalid payment type
    with pytest.raises(ValueError):
        order.set_pay_type('INVALID')

def test_get_invalid_payment_type(order):
    # Test getting invalid payment type
    order.set_pay_type('CARD')
    order._pay_type = 'INVALID'
    with pytest.raises(ValueError):
        order.get_pay_type()

def test_default_payment_type(order):
    # Test default payment type
    assert order.get_pay_type() == 'CASH'

def test_order_sort(order):
    # Add some items to the order in unsorted order
    order.add(Candy("Candy 1", 0.5, 2.99))
    order.add(Candy("Candy 2", 0.3, 1.99))
    order.add(Candy("Candy 3", 0.8, 3.49))

    # Sort the order
    order.sort()

    # Get the list of items after sorting
    sorted_items = [item.name for item in order.order]

    # Expected order after sorting
    expected_order = ["Candy 2", "Candy 1", "Candy 3"]

    # Check if the items are sorted correctly
    assert sorted_items == expected_order

if __name__ == "__main__":
    pytest.main()