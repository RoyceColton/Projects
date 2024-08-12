from typing import Union, Literal
from typing_extensions import Protocol

PayType = Literal['CASH', 'CARD', 'PHONE']

class Payable(Protocol):
    _pay_type: PayType  # Declare _pay_type within the class body

    def __init__(self):
        self._pay_type = "CASH"  # Defaulting to "CASH"

    def get_pay_type(self) -> PayType:
        if self._pay_type not in ['CASH', 'CARD', 'PHONE']:
            raise ValueError("Invalid payment type detected")
        return self._pay_type

    def set_pay_type(self, payment_method: PayType) -> None:
        if payment_method not in ['CASH', 'CARD', 'PHONE']:
            raise ValueError("Invalid payment method. Must be one of: CASH, CARD, PHONE")
        self._pay_type = payment_method