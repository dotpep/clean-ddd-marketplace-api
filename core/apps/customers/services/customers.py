from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.customers.entities import CustomerEntity
from core.apps.customers.models import CustomerModel


class BaseCustomerService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> CustomerEntity:
        pass

    @abstractmethod
    def get(self, phone: str) -> CustomerEntity:
        pass

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str:
        pass


class ORMCustomerService(BaseCustomerService):
    def get_or_create(self, phone: str) -> CustomerEntity:
        customer_dto, _ = CustomerModel.objects.get_or_create(phone=phone)
        return customer_dto.to_entity()

    def get(self, phone: str) -> CustomerEntity:
        customer_dto = CustomerModel.objects.get(phone=phone)
        return customer_dto.to_entity()

    def generate_token(self, customer: CustomerEntity) -> str:
        new_token = str(uuid4())
        CustomerModel.objects.filter(phone=customer.phone).update(
            token=new_token,
        )
        return new_token
