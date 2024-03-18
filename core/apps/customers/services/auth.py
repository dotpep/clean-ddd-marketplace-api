from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.customers.services.codes import BaseCodeService
from core.apps.customers.services.customers import BaseCustomerService
from core.apps.customers.services.senders import BaseSenderService


@dataclass(eq=False)
class BaseAuthService(ABC):
    # Initialize services
    customer_service = BaseCustomerService
    code_service = BaseCodeService
    sender_service = BaseSenderService

    @abstractmethod
    def authorize(self, phone: str) -> None:
        pass

    @abstractmethod
    def confirm(self, token: str) -> None:
        pass


class AuthService(BaseAuthService):
    pass
