from datetime import datetime

from django.http import HttpRequest
from ninja import (
    Header,
    Router,
)
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import (
    CreateReviewSchema,
    ReviewInSchema,
    ReviewOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.products.services.reviews import BaseReviewService
from core.project.containers import get_container


router = Router(tags=['Reviews'])


@router.post('{product_id}/reviews', response=ApiResponse[ReviewOutSchema], operation_id="createReview")
def create_review_on_product_handler(
    request: HttpRequest,
    product_id: int,
    schema: ReviewInSchema,
    token: str = Header(alias='Auth-Token'),
) -> ApiResponse[ReviewOutSchema]:
    create_schema = CreateReviewSchema(
        product_id=product_id,
        client_token=token,
        review=schema,
    )
    container = get_container()
    service: BaseReviewService = container.resolve(BaseReviewService)
    print(create_schema)

    try:
        result = service.create_review(
            product_id=schema.product_id,
            customer_token=token,
            rating=schema.rating,
            text=schema.text,
        )
        print(result)
    except ServiceException as error:
        raise HttpError(status_code=400, message=error.message)

    return ApiResponse(
        data=ReviewOutSchema(
            rating=3,
            text='Very good product',
            id=1,
            created_at=datetime.now(),
            updated_at=None,
        ),
    )
