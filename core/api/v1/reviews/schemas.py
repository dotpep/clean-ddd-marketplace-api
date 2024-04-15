from datetime import datetime

from ninja import Schema

from core.apps.products.entities.reviews import ReviewEntity


class ReviewInSchema(Schema):
    rating: int
    text: str

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(text=self.text, rating=self.rating)


class CreateReviewSchema(Schema):
    product_id: int
    client_token: str
    reviw: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int  # noqa
    created_at: datetime
    updated_at: datetime | None

    @classmethod
    def from_entity(cls, review: ReviewEntity) -> 'ReviewOutSchema':
        return cls(
            id=review.id,
            text=review.text,
            rating=review.rating,
            created_at=review.created_at,
            updated_at=review.updated_at,
        )
