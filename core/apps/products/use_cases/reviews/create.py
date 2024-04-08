from abc import ABC
from dataclasses import dataclass

from core.apps.customers.services.customers import BaseCustomerService
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.services.products import BaseProductService
from core.apps.products.services.reviews import BaseReviewService


@dataclass
class CreateReviewUseCase(ABC):
    review_service = BaseReviewService
    customer_service = BaseCustomerService
    product_service = BaseProductService

    def execute(
        self,
        product_id: int,
        customer_token: str,
        rating: int,
        text: str,
    ) -> ReviewEntity:
        # Get product from ID
        # Check validation of client token
        # Check rating range 1 <= R <= 5
        # Check text length and censure
        customer = self.customer_service.get_by_token(token=customer_token)
        product = self.product_service.get_by_id(product_id=product_id)
        review = self.review_service.create_review(
            product=product,
            customer=customer,
            rating=rating,
            text=text,
        )

        return review
