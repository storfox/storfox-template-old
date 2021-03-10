import typing
from storfox_framework import db

import schemes
import application.entities as entities


async def create_customer(customer: entities.Customer) -> entities.Customer:
    # TODO: create customer, create addresses
    schemes.customer.create()

    return entities.Customer()
