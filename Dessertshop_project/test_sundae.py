import pytest
from dessert import Sundae

def test_sundae_constructor():
    """Test if Sundae sets the name, scoop count, topping, and topping price correctly."""
    sundae = Sundae("Test Sundae", 2, 3.99, "Test Topping", 0.99)
    assert sundae.name == "Test Sundae"
    assert sundae.scoop_count == 2
    assert sundae.topping_name == "Test Topping"
    assert sundae.topping_price == 0.99

def test_sundae_calculate_cost():
    """Test if Sundae calculates cost correctly."""
    sundae = Sundae("Sundae Test", 2, 3.99, "Chocolate Sauce", 0.99)
    assert sundae.calculate_cost() == pytest.approx(8.97)

def test_sundae_calculate_tax():
    """Test if Sundae calculates tax correctly."""
    sundae = Sundae("Sundae Test", 2, 3.99, "Chocolate Sauce", 0.99)
    assert sundae.calculate_tax() == pytest.approx(0.650775, 0.01)