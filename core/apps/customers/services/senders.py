from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from core.apps.customers.entities import CustomerEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        pass


class DummySenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to customer: {customer=}, sent: {code=}")


@dataclass
class SMSExampleSenderService(BaseSenderService):
    """Example of sender service using SMS to punq package DI pattern with attributes secret_token
    usage in DI container:
    container.register(BaseSenderService, SMSExampleSenderService, secret_token='super_secret_token_args')"""
    secret_token: str

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to customer: {customer=}, sent: {code=} with attributes {self.secret_token=} via SMS")


class EmailExampleSenderService(BaseSenderService):
    """Example of sender service using Email."""
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Send {code=} to customer email: customeremail@hardcoded.com")


class PushExampleSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Send push notification with {code=} fcm_token")


@dataclass
class CompositeSenderService(BaseSenderService):
    """Send with multiple Sender Service using Composite Pattern."""
    sender_services: Iterable[BaseSenderService]

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        for service in self.sender_services:
            service.send_code(customer, code)
