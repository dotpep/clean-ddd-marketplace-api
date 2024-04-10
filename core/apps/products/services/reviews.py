from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.exceptions.reviews import ReviewInvalidRatingException


class BaseReviewService(ABC):
    @abstractmethod
    def save_review(
        self,
        review: ReviewEntity,
        customer: CustomerEntity,
        product: ProductEntity,
    ) -> ReviewEntity:
        pass


class ReviewService(BaseReviewService):
    def create_review(
        self,
        product_id: int,
        customer_token: str,
        rating: str,
        text: str,
    ) -> ReviewEntity:
        pass


class BaseReviewValidatorService(ABC):
    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ):
        pass


class ReviewRatingValidatorService(BaseReviewValidatorService):
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ):
        # TODO: constants for range of rating
        if not (1 <= review.rating <= 5):
            raise ReviewInvalidRatingException(rating=review.rating)


class CompositeReviewValidatorService(BaseReviewValidatorService):
    validators: list[BaseReviewValidatorService]

    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ):
        for validator in self.validators:
            validator.validate(review=review, customer=customer, product=product)
