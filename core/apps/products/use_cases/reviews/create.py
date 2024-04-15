from dataclasses import dataclass

from core.apps.customers.services.customers import ORMCustomerService
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.services.products import ORMProductService
from core.apps.products.services.reviews import (
    CompositeReviewValidatorService,
    ORMReviewService,
)


# To Initialize DI container dependencies you must use (ABC) module or @dataclass decorator
# In case of Base Auth Service dependencies DI we use @dataclass with (eq=False) parameter and ABC
@dataclass
class CreateReviewUseCase:
    #review_service = BaseReviewService  # noqa
    #customer_service = BaseCustomerService  # noqa
    #product_service = BaseProductService  # noqa
    #validator_service = BaseReviewValidatorService  # noqa

    # FIXME: punq container cannot initialize dependencies and
    # create insance of provided BaseService ABC class with dependency also
    # review_service Base Interface is BaseReviewService and implementation is ORMReviewService
    review_service = ORMReviewService()  # fix this line and delete
    customer_service = ORMCustomerService()  # fix this line and delete
    product_service = ORMProductService()  # fix this line and delete
    validator_service = CompositeReviewValidatorService()  # fix this line and delete

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

        # FIXME: In sometimes it occurs again when fetching api handler endpoints of create_review
        # FIXME: Trouble with initalizating the customer service (ORMCustomerService) to execute instance of method instead Class  # noqa
        # maybe is because Dependency Injection container does not working well and miss initilization of ORMCustomerService  # noqa
        # class Employee: def display(self): pass john = Employee(name='John') Employee.display()  # noqa
        # correction is using instance of Employee john to use display method: john.display()  # noqa
        # https://stackoverflow.com/questions/70685994/python-class-showing-missing-1-required-positional-argument-self  # noqa
        # when you hover mouse on get_by_token method it shows that requires argument: get_by_token(self: customer_service, token: str)  # noqa
        # customer_service().get_by_token(token=customer_token)  # noqa

        customer = self.customer_service.get_by_token(token=customer_token)
        product = self.product_service.get_by_id(product_id=product_id)

        self.validator_service.validators = []  # fix this line and delete
        self.validator_service.validate(review=review, customer=customer, product=product)

        saved_review = self.review_service.save_review(review=review, customer=customer, product=product)

        return saved_review
