from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import Product as ProductEntity


# DTO (Data Transfer Object)
class Product(TimedBaseModel):
    title = models.CharField(
        verbose_name='Название товара',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание товара',
        blank=True,
    )
    is_visible = models.BooleanField(
        verbose_name='Виден ли товар в каталоге',
        default=True,
    )

    # simplified version of converter in DDD architecture for DTO (Entity)
    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
