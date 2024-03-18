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
    def confirm(self, code: str, phone: str) -> None | str:
        pass


class AuthService(BaseAuthService):
    def authorize(self, phone: str) -> None:
        customer = self.customer_service.get_or_create(phone=phone)
        code = self.code_service.generate_code(customer=customer)
        self.sender_service.send_code(code=code)

    def confirm(self, code: str, phone: str) -> None | str:
        customer = self.customer_service.get(phone=phone)
        self.code_service.validate_code(code=code, customer=customer)
        return self.customer_service.generate_token(customer=customer)
