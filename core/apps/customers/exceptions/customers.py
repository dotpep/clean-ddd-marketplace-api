from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CustomerTokenInvalidException(ServiceException):
    token: str

    @property
    def message(self):
        return "A customer with provided token is not found or invalid."
