from datetime import datetime

from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import (
    ReviewInSchema,
    ReviewOutSchema,
)


router = Router(tags=['Reviews'])


@router.post('{product_id}/reviews', response=ApiResponse[ReviewOutSchema], operation_id="createReview")
def create_review_on_product_handler(
    request: HttpRequest,
    product_id: int,
    schema: ReviewInSchema,
) -> ApiResponse[ReviewOutSchema]:
    return ApiResponse(
        data=ReviewOutSchema(
            rating=3,
            text='Very good product',
            id=1,
            created_at=datetime.now(),
            updated_at=None,
        ),
    )
