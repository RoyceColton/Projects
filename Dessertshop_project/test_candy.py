import pytest
from dessert import Candy

def test_candy_constructor():
    """Test if Candy sets the name, weight, and price per pound correctly."""
    candy = Candy("Test Candy", 0.5, 2.99)
    assert candy.name == "Test Candy"
    assert candy.weight == 0.5
    assert candy.price_per_pound == 2.99

def test_candy_calculate_cost():
    """Test if Candy calculates cost correctly."""
    candy = Candy("Chocolate Bar", 0.5, 2.99)
    assert candy.calculate_cost() == pytest.approx(1.495, 0.01)

def test_candy_calculate_tax():
    """Test if Candy calculates tax correctly."""
    candy = Candy("Test Candy", 0.5, 2.99)
    assert candy.calculate_tax() == pytest.approx(0.1083875, 0.01)

# New tests for Combinable functionality

def test_can_combine_both_candies():
    """Test if can_combine() returns True if both items are candies."""
    candy1 = Candy("Chocolate", 1, 10)
    candy2 = Candy("Chocolate", 2, 10)
    assert candy1.can_combine(candy2) == True

def test_can_combine_other_not_candy():
    """Test if can_combine() returns False if the other item is not a Candy."""
    candy = Candy("Chocolate", 1, 10)
    other_item = "Not a Candy"
    assert candy.can_combine(other_item) == False

def test_combine_two_candies():
    """Test if combine() correctly combines two Candy items."""
    candy1 = Candy("Chocolate", 1, 10)
    candy2 = Candy("Chocolate", 2, 10)
    candy1.combine(candy2)
    assert candy1.weight == 3

def test_combine_candy_with_non_candy():
    """Test if combine() correctly fails when combining a Candy with a non-Candy item."""
    candy = Candy("Chocolate", 1, 10)
    other_item = "Not a Candy"
    with pytest.raises(ValueError):
        candy.combine(other_item)