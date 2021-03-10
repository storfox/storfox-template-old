from dataclasses import dataclass
from storfox_framework.value_object import ValueObject


@dataclass
class Address(ValueObject):
    first_name: str
    last_name: str
    phone_number: str
    address: str
    city: str
    country: str
