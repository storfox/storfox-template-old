import typing
from datetime import date

from attr import dataclass
from betterproto import Casing
from pydantic import BaseModel

import genproto.customer as customer_pb


class BaseDto(BaseModel):
    @classmethod
    def from_request(cls, request: typing.Any) -> typing.Any:
        raise NotImplemented

    def to_response(self) -> typing.Any:
        raise NotImplemented


class CustomerCreateReqDto(BaseDto):
    class Address(BaseModel):
        first_name: str
        last_name: str
        phone_number: str
        address: str
        zip_code: str
        city: str
        country: str

    first_name: str
    last_name: str
    birth_date: date
    shipping_addresses: typing.List[Address]
    billing_addresses: typing.List[Address]

    @classmethod
    def from_request(cls, request: typing.Any) -> "CustomerCreateReqDto":
        return cls(**request.data.to_dict(casing=Casing.SNAKE))


class CustomerCreateResDto(BaseDto):
    class Address(BaseModel):
        first_name: str
        last_name: str
        phone_number: str
        address: str
        zip_code: str
        city: str
        country: str

    first_name: str
    last_name: str
    birth_date: date
    shipping_addresses: typing.List[Address]
    billing_addresses: typing.List[Address]

    def to_response(self) -> "customer_pb.CustomerCreateResponse":
        return customer_pb.CustomerCreateResponse()


@dataclass
class CustomerDto:
    pass
