from dataclasses import dataclass
from storfox_framework.value_object import ValueObject


@dataclass
class Email(ValueObject):
    value: str

    def __str__(self):
        return self.value
