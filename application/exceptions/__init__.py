class CustomerNotFound(Exception):
    code = 3
    message = "Customer not found."


class InvalidLocation(Exception):
    code = 3
    message = "Invalid location."
