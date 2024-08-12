import pytest
from dessert import Cookie

def test_cookie_constructor():
    """Test if Cookie sets the name, quantity, and price per dozen correctly."""
    cookie = Cookie("Test Cookie", 12, 4.99)
    assert cookie.name == "Test Cookie"
    assert cookie.quantity == 12
    assert cookie.price_per_dozen == 4.99

def test_cookie_calculate_cost():
    """Test if Cookie calculates cost correctly."""
    cookie = Cookie("Chocolate Chip", 12, 4.99)
    assert cookie.calculate_cost() == pytest.approx(4.99)

def test_cookie_calculate_tax():
    """Test if Cookie calculates tax correctly."""
    cookie = Cookie("Chocolate Chip", 12, 4.99)
    assert cookie.calculate_tax() == pytest.approx(0.361125, 0.01)

# New tests for Combinable functionality

def test_can_combine_both_cookies():
    """Test if can_combine() returns True if both items are cookies."""
    cookie1 = Cookie("Chocolate Chip", 12, 5)
    cookie2 = Cookie("Chocolate Chip", 24, 5)
    assert cookie1.can_combine(cookie2) == True

def test_can_combine_other_not_cookie():
    """Test if can_combine() returns False if the other item is not a Cookie."""
    cookie = Cookie("Chocolate Chip", 12, 5)
    other_item = "Not a Cookie"
    assert cookie.can_combine(other_item) == False

def test_combine_two_cookies():
    """Test if combine() correctly combines two Cookie items."""
    cookie1 = Cookie("Chocolate Chip", 12, 5)
    cookie2 = Cookie("Chocolate Chip", 24, 5)
    combined_cookie = cookie1.combine(cookie2)
    assert combined_cookie.quantity == 36

def test_combine_cookie_with_non_cookie():
    """Test if combine() correctly fails when combining a Cookie with a non-Cookie item."""
    cookie = Cookie("Chocolate Chip", 12, 5)
    other_item = "Not a Cookie"
    with pytest.raises(ValueError):
        cookie.combine(other_item)