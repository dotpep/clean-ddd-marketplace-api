from abc import ABC
from dataclasses import dataclass

from core.apps.customers.services.customers import BaseCustomerService
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.services.products import BaseProductService
from core.apps.products.services.reviews import (
    BaseReviewService,
    BaseReviewValidatorService,
)


@dataclass
class CreateReviewUseCase(ABC):
    review_service = BaseReviewService
    customer_service = BaseCustomerService
    product_service = BaseProductService
    validator_service = BaseReviewValidatorService

    def execute(
        self,
        product_id: int,
        customer_token: str,
        review: ReviewEntity,
    ) -> ReviewEntity:
        # Get product from ID
        # Check validation of client token
        # Check rating range 1 <= R <= 5
        # Check text length and censure
        customer = self.customer_service.get_by_token(token=customer_token)
        product = self.product_service.get_by_id(product_id=product_id)

        self.validator_service.validate(review=review, customer=customer, product=product)

        saved_review = self.review_service.save_review(review=review, customer=customer, product=product)

        return saved_review
