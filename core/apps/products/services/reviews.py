from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.exceptions.reviews import ReviewInvalidRatingException
from core.apps.products.models.reviews import ReviewModel


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
    def save_review(
        self,
        review: ReviewEntity,
        customer: CustomerEntity,
        product: ProductEntity,
    ) -> ReviewEntity:
        review_dto: ReviewModel = ReviewModel.from_entity(
            review=review,
            customer=customer,
            product=product,
        )
        review_dto.save()
        return review_dto.to_entity()


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
