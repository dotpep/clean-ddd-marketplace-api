from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import CustomerEntity


class CustomerModel(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=20,
        unique=True,
    )
    token = models.CharField(
        verbose_name='User Auth Token',
        max_length=255,
        unique=True,
        default=uuid4,
    )

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            phone=self.phone,
            created_at=self.created_at,
        )

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
