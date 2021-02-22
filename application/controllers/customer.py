from genproto.customer import CustomerServiceBase
from genproto.customer import CustomerCreateResponse
from genproto.customer import CustomerDetailResponse
from genproto.customer import CustomerListResponse
from genproto.customer import CustomerUpdateResponse
from genproto.customer import CustomerDeleteResponse


class CustomerController(CustomerServiceBase):
    async def detail_customer(self, **kwargs) -> "CustomerDetailResponse":
        return CustomerDetailResponse()

    async def list_customer(self, **kwargs) -> "CustomerListResponse":
        return CustomerListResponse()

    async def create_customer(self, **kwargs) -> "CustomerCreateResponse":
        return CustomerCreateResponse()

    async def update_customer(self, **kwargs) -> "CustomerUpdateResponse":
        return CustomerUpdateResponse()

    async def delete_customer(self, **kwargs) -> "CustomerDeleteResponse":
        return CustomerDeleteResponse()
