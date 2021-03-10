import datetime
import typing
import uuid
from dataclasses import dataclass
from application.value_objects.address import Address


@dataclass
class Customer(object):
    guid: typing.Optional[uuid.UUID]
    first_name: str
    last_name: str
    birth_date: datetime.date
    shipping_addresses: typing.Optional[typing.List[Address]]
    billing_addresses: typing.Optional[typing.List[Address]]
    updated_at: typing.Optional[datetime.datetime]
    created_at: typing.Optional[datetime.datetime]
