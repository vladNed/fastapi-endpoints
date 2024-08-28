
class BaseOSException(Exception):
    message: str

    def __init__(self):
        super().__init__(self.message)


class InitializationError(BaseOSException):
    message = "Could not init the FastAPI app"


class RouterDirNotFound(BaseOSException):
    message = "Routers directory is not defined"
