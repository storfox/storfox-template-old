from dataclasses import dataclass
from storfox_framework.value_object import ValueObject


@dataclass
class Phone(ValueObject):
    value: str
