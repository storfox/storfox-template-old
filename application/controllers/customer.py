import application.services.customer as svc
import genproto.customer as customer_pb
import application.dtos as customer_dto
from storfox_framework import current_app as app


def handle_error(func):
    request_type = func.__annotations__["request"]
    reply_type = func.__annotations__["return"]

    async def wrapper(request: request_type) -> reply_type:
        try:
            return await func(request)
        except Exception:
            raise

    return wrapper


@app.grpc("/customer.CustomerService/DetailCustomer")
async def detail(
    request: customer_pb.CustomerDetailRequest,
) -> customer_pb.CustomerDetailResponse:
    return customer_pb.CustomerDetailResponse(code=0)


@app.grpc("/customer.CustomerService/ListCustomer")
async def list_customer(
    request: customer_pb.CustomerListRequest,
) -> customer_pb.CustomerListResponse:
    return customer_pb.CustomerListResponse()


@app.grpc("/customer.CustomerService/CreateCustomer")
@handle_error
async def create_customer(
    request: customer_pb.CustomerCreateRequest,
) -> customer_pb.CustomerCreateResponse:
    req_dto = customer_dto.CustomerCreateReqDto.from_request(request)
    res_dto = await svc.create_customer(req_dto)
    return res_dto.to_response()


@app.grpc("/customer.CustomerService/UpdateCustomer")
async def update_customer(
    request: customer_pb.CustomerUpdateRequest,
) -> customer_pb.CustomerUpdateResponse:
    return customer_pb.CustomerUpdateResponse()


@app.grpc("/customer.CustomerService/DeleteCustomer")
async def delete_customer(
    request: customer_pb.CustomerDeleteRequest,
) -> customer_pb.CustomerDeleteResponse:
    return customer_pb.CustomerDeleteResponse()
