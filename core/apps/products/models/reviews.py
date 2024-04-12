from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity


class ReviewModel(TimedBaseModel):
    customer = models.ForeignKey(
        to='customers.CustomerModel',
        verbose_name='Reviewer',
        related_name='product_reviews',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to='products.ProductModel',
        verbose_name='Product',
        related_name='product_reviews',
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Rating',
        default=1,
    )
    text = models.TextField(
        verbose_name='Review text',
        blank=True,
        default='',
    )

    # TODO: take only review
    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
        customer: CustomerEntity,
        product: ProductEntity,
    ) -> 'ReviewModel':
        return cls(
            pk=review.id,
            customer_id=customer.id,
            product_id=product.id,
            text=review.text,
            rating=review.rating,
        )

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            id=self.id,
            text=self.text,
            rating=self.rating,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self):
        return str(self.customer) + ' ' + str(self.product)

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'
        unique_together = (
            ('customer', 'product'),
        )
