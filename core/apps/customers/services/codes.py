from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import CustomerEntity


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str:
        pass

    @abstractmethod
    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        pass
