import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from core.apps.customers.entities import CustomerEntity
from core.apps.customers.exceptions.codes import (
    CodeNotEqualException,
    CodeNotFoundException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str:
        pass

    @abstractmethod
    def validate_code(self, code: str, customer: CustomerEntity) -> None:  # bool
        pass


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, customer: CustomerEntity) -> str:
        secure_random = random.SystemRandom()
        code = str(secure_random.randint(100000, 999999))
        cache.set(customer.phone, code)
        return code

    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        cached_code = cache.get(customer.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if cached_code != code:
            raise CodeNotEqualException(code=code, customer=customer, customer_phone=customer.phone)

        cache.delete(customer.phone)
