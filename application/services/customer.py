import application.repositories.customer as repo
import application.dtos as customer_dto
from application.dtos import CustomerCreateResDto
import application.entities as entities
import application.value_objects as value_objects


async def create_customer(
        customer_req_dto: customer_dto.CustomerCreateReqDto,
) -> customer_dto.CustomerCreateResDto:
    await _validate(customer_req_dto)
    await repo.create_customer(
        entities.Customer(
            first_name=customer_req_dto.first_name,
            last_name=customer_req_dto.last_name,
            birth_date=customer_req_dto.birth_date,
            shipping_addresses=[
                value_objects.CustomerAddress(
                    address.first_name,
                    address.last_name,
                    address.phone_number,
                    address.address,
                    address.city,
                    address.country
                )
                for address in customer_req_dto.shipping_addresses
            ],
            billing_addresses=[
                value_objects.CustomerAddress(
                    address.first_name,
                    address.last_name,
                    address.phone_number,
                    address.address,
                    address.city,
                    address.country
                )
                for address in customer_req_dto.billing_addresses
            ],
            updated_at=None,
            created_at=None,
            guid=None
        )
    )
    dto = CustomerCreateResDto()

    return dto


async def _validate(dto):
    pass
