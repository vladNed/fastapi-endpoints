# fastapi-endpoints
# Copyright (c) 2024 Vlad Nedelcu
# Licensed under the MIT License


class BaseOSException(Exception):
    """The base exception used to manage the message in a dynamic way"""

    message: str

    def __init__(self):
        super().__init__(self.message)


class InitializationError(BaseOSException):
    """Error for any issue that comes when the routers are being fetched
    and included in the app
    """

    message = "Could not initialize routes as modules are not defined correctly"


class RouterNotFound(BaseOSException):
    """FastAPI APIRouter instance is not found in the router file
    module.
    """

    message = "Router module does not have an instance of APIRouter"
