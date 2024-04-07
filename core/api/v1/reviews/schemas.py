from datetime import datetime

from ninja import Schema


class ReviewInSchema(Schema):
    rating: int
    text: str


class CreateReviewSchema(Schema):
    product_id: int
    client_token: str
    reviw: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int  # noqa
    created_at: datetime
    updated_at: datetime | None
