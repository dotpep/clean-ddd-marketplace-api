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

        # FIXME: Trouble with initalizating the customer service (ORMCustomerService) to execute instance of method instead Class  # noqa
        # maybe is because Dependency Injection container does not working well and miss initilization of ORMCustomerService  # noqa
        # class Employee: def display(self): pass john = Employee(name='John') Employee.display()  # noqa
        # correction is using instance of Employee john to use display method: john.display()  # noqa
        # https://stackoverflow.com/questions/70685994/python-class-showing-missing-1-required-positional-argument-self  # noqa
        # when you hover mouse on get_by_token method it shows that requires argument: get_by_token(self: customer_service, token: str)  # noqa
        # customer_service().get_by_token(token=customer_token)  # noqa

        customer = self.customer_service.get_by_token(token=customer_token)
        product = self.product_service.get_by_id(product_id=product_id)

        self.validator_service.validate(review=review, customer=customer, product=product)

        saved_review = self.review_service.save_review(review=review, customer=customer, product=product)

        return saved_review
