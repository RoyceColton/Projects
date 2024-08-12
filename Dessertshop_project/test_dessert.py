import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_dessert_item_constructor():
    """Test if DessertItem sets the name correctly."""
    dessert = Candy("Generic Dessert", 0.5, 2.99)
    assert dessert.name == "Generic Dessert"

def test_candy_inheritance():
    """Test if Candy inherits from DessertItem."""
    candy = Candy("Candy Test", 1.0, 5.99)
    assert isinstance(candy, DessertItem)

def test_dessert_item_tax_percent():
    """Test if DessertItem has the correct default tax percent."""
    assert DessertItem.tax_percent == 0.0725

def test_candy_calculate_cost():
    """Test if Candy calculates cost correctly."""
    candy = Candy("Chocolate Bar", 0.5, 2.99)
    assert candy.calculate_cost() == pytest.approx(1.495, 0.01)

def test_candy_calculate_tax():
    """Test if Candy calculates tax correctly."""
    candy = Candy("Test Candy", 0.5, 2.99)
    assert candy.calculate_tax() == pytest.approx(0.1083875, 0.01)

def test_cookie_calculate_cost():
    """Test if Cookie calculates cost correctly."""
    cookie = Cookie("Chocolate Chip", 12, 4.99)
    assert cookie.calculate_cost() == pytest.approx(4.99)

def test_cookie_calculate_tax():
    """Test if Cookie calculates tax correctly."""
    cookie = Cookie("Chocolate Chip", 12, 4.99)
    assert cookie.calculate_tax() == pytest.approx(0.361125, 0.01)

def test_icecream_calculate_cost():
    """Test if IceCream calculates cost correctly."""
    icecream = IceCream("Vanilla", 2, 3.99)
    assert icecream.calculate_cost() == pytest.approx(7.98)

def test_icecream_calculate_tax():
    """Test if IceCream calculates tax correctly."""
    icecream = IceCream("Vanilla", 2, 3.99)
    assert icecream.calculate_tax() == pytest.approx(0.57855, 0.01)

def test_sundae_calculate_cost():
    """Test if Sundae calculates cost correctly."""
    sundae = Sundae("Sundae Test", 2, 3.99, "Chocolate Sauce", 0.99)
    assert sundae.calculate_cost() == pytest.approx(8.97)

def test_sundae_calculate_tax():
    """Test if Sundae calculates tax correctly."""
    sundae = Sundae("Sundae Test", 2, 3.99, "Chocolate Sauce", 0.99)
    assert sundae.calculate_tax() == pytest.approx(0.650775, 0.01)

def test_dessert_item_equality():
    """Test if DessertItem equality operator works correctly."""
    candy1 = Candy("Candy 1", 0.5, 2.99)
    candy2 = Candy("Candy 2", 0.5, 2.99)
    assert candy1 == candy2

def test_dessert_item_inequality():
    """Test if DessertItem inequality operator works correctly."""
    candy1 = Candy("Candy 1", 0.5, 2.99)
    candy2 = Candy("Candy 2", 0.5, 2.99)
    assert candy1 != candy2

def test_dessert_item_less_than():
    """Test if DessertItem less than operator works correctly."""
    candy1 = Candy("Candy 1", 0.5, 2.99)
    candy2 = Candy("Candy 2", 0.6, 2.99)
    assert candy1 < candy2

def test_dessert_item_less_than_or_equal():
    """Test if DessertItem less than or equal to operator works correctly."""
    candy1 = Candy("Candy 1", 0.5, 2.99)
    candy2 = Candy("Candy 2", 0.5, 2.99)
    assert candy1 <= candy2

def test_dessert_item_greater_than():
    """Test if DessertItem greater than operator works correctly."""
    candy1 = Candy("Candy 1", 0.6, 2.99)
    candy2 = Candy("Candy 2", 0.5, 2.99)
    assert candy1 > candy2

def test_dessert_item_greater_than_or_equal():
    """Test if DessertItem greater than or equal to operator works correctly."""
    candy1 = Candy("Candy 1", 0.5, 2.99)
    candy2 = Candy("Candy 2", 0.5, 2.99)
    assert candy1 >= candy2