from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payable
from combine import Combinable

class DessertItem(ABC): 
    tax_percent = 0.0725  # represent the 7.25% tax

    def __init__(self, name):
        self.name = name
        self.packaging = None

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * DessertItem.tax_percent

    def __eq__(self, other):
        return self.calculate_cost() == other.calculate_cost()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.calculate_cost() < other.calculate_cost()

    def __gt__(self, other):
        return self.calculate_cost() > other.calculate_cost()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
class Candy(DessertItem):  
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.weight = weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"

    def calculate_cost(self):
        return self.weight * self.price_per_pound
    
    def can_combine(self, other: "Candy") -> bool:
        return (
            isinstance(other, Candy) and
            self.name == other.name and 
            self.price_per_pound == other.price_per_pound
        )
    
    def combine(self, other: "Candy") -> "Candy":
        if not self.can_combine(other):
            raise ValueError("Cannot combine candies with different attributes")
        # Implement the combination logic here

    def __str__(self):
        return f"{self.name}, {self.weight} lbs, ${self.price_per_pound:.2f}/lb, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

class Cookie(DessertItem):  
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def calculate_cost(self):
        return self.quantity * (self.price_per_dozen / 12)

    def can_combine(self, other: "Cookie") -> bool:
        return(
            isinstance(other, Cookie) and
            self.name == other.name and
            self.price_per_dozen == other.price_per_dozen
        )
    
    def combine(self, other: "Cookie") -> "Cookie":
        if not self.can_combine(other):
            raise ValueError("Cannot combine cookies with different attributes")
        # Implement the combination logic here

    def __str__(self):
        return f"{self.name}, {self.quantity} cookies, ${self.price_per_dozen:.2f}/dozen, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.packaging}"

class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "bowl"

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop

    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.packaging}"

class Sundae(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop + self.topping_price

    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.topping_name}, ${self.topping_price:.2f}, {self.packaging}"

class Order:
    def __init__(self):
        self.order = []
        self.payment_type = None

    def set_pay_type(self, payment_type):
        self.payment_type = payment_type
    def get_pay_type(self):
        return self.payment_type

    def add(self, item):
        if isinstance(item, Combinable):  
            combined = False
            for existing_item in self.order:
                if existing_item.can_combine(item):
                    combined_item = existing_item.combine(item)
                    self.order.remove(existing_item)  # Remove the old item
                    self.order.append(combined_item)  # Add the combined item
                    combined = True
                    break
            if not combined:
                self.order.append(item)
        else:
            self.order.append(item)

    def __len__(self):
        ''' Returns the number of items in the order'''
        return len(self.order)

    def __iter__(self):
        '''Returns an iterator for the order'''
        self._index = 0
        return self

    def __next__(self):
        '''
        Returns the next item in the order using the iterator
        until there are no more
        '''
        if self._index < len(self.order):
            item = self.order[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def order_cost(self):
        '''Calculates and returns the total cost for all items in the order'''
        total_cost = sum(item.calculate_cost() for item in self.order)
        return total_cost

    def order_tax(self):
        '''Calculates and returns the total tax for all items in the order'''
        total_tax = sum(item.calculate_tax() for item in self.order)
        return total_tax

    def sort(self):
        '''Sorts the dessert items in the order by price'''
        self.order.sort(key=lambda item: item.calculate_cost())

    def __str__(self):
        '''Returns a string representation of the order'''
        payment_info = (f"Payment Type: {self.get_pay_type()}\n")
        items_info = '\n'.join(str(item) for item in self.order)
        return payment_info + items_info