from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from core.apps.common.enums import EntityStatusEnum
from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity


@dataclass
class ReviewEntity:
    """Domain Entity of Product Review."""
    id: int | None = field(default=None, kw_only=True)  # noqa
    customer: CustomerEntity | EntityStatusEnum = field(default=EntityStatusEnum.NOT_LOADED)
    product: ProductEntity | EntityStatusEnum = field(default=EntityStatusEnum.NOT_LOADED)

    text: str = field(default='')
    rating: int = field(default=1)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default=None)
