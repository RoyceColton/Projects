import pytest
from dessert import IceCream

def test_icecream_constructor():
    """Test if IceCream sets the name, scoop count, and price per scoop correctly."""
    icecream = IceCream("Test Ice Cream", 2, 3.99)
    assert icecream.name == "Test Ice Cream"
    assert icecream.scoop_count == 2
    assert icecream.price_per_scoop == 3.99

def test_icecream_calculate_cost():
    """Test if IceCream calculates cost correctly."""
    icecream = IceCream("Vanilla", 2, 3.99)
    assert icecream.calculate_cost() == pytest.approx(7.98)

def test_icecream_calculate_tax():
    """Test if IceCream calculates tax correctly."""
    icecream = IceCream("Vanilla", 2, 3.99)
    assert icecream.calculate_tax() == pytest.approx(0.57855, 0.01)