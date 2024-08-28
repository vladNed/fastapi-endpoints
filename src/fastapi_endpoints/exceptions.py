# fastapi-endpoints
# Copyright (c) 2024 Vlad Nedelcu
# Licensed under the MIT License


class BaseOSException(Exception):
    message: str

    def __init__(self):
        super().__init__(self.message)


class InitializationError(BaseOSException):
    message = "Could not initialize routes as modules are not defined correctly"


class RouterNotFound(BaseOSException):
    message = "Router module does not have an instance of APIRouter"
