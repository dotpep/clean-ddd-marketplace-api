from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import CustomerEntity


class BaseCustomerService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> CustomerEntity:
        pass

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str:
        pass
