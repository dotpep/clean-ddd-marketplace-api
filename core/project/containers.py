from functools import lru_cache

import punq

from core.apps.customers.services.auth import (
    AuthService,
    BaseAuthService,
)
from core.apps.customers.services.codes import (
    BaseCodeService,
    DjangoCacheCodeService,
)
from core.apps.customers.services.customers import (
    BaseCustomerService,
    ORMCustomerService,
)
from core.apps.customers.services.senders import (
    BaseSenderService,
    CompositeSenderService,
    EmailExampleSenderService,
    PushExampleSenderService,
)
from core.apps.products.services.products import (
    BaseProductService,
    ORMProductService,
)
from core.apps.products.services.reviews import (
    BaseReviewService,
    BaseReviewValidatorService,
    CompositeReviewValidatorService,
    ORMReviewService,
)
from core.apps.products.use_cases.reviews.create import CreateReviewUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    """Dependency injection container for service."""
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # Initialize Services
    # Initialize products
    container.register(BaseProductService, ORMProductService)
    # Initialize customers
    container.register(BaseCustomerService, ORMCustomerService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    # Usage with providing attribute for Service: SMSExampleSenderService, secret_token='super_secret_token_args'
    # Using Composite Service that handle multiple sender services (Composite Pattern in DI)
    container.register(
        BaseSenderService,
        CompositeSenderService,
        sender_services=(
            PushExampleSenderService(),
            EmailExampleSenderService(),
        ),
    )
    container.register(BaseAuthService, AuthService)
    # Initialize reviews
    container.register(BaseReviewService, ORMReviewService)
    container.register(BaseReviewValidatorService, CompositeReviewValidatorService, validators=[])

    # Initialize Use Cases
    container.register(CreateReviewUseCase)

    return container
