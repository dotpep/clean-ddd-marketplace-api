from dataclasses import (
    dataclass,
    field,
)

from core.apps.common.enums import EntityStatusEnum
from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity


@dataclass
class ReviewEntity:
    """Domain Entity of Product Review."""
    customer: CustomerEntity | EntityStatusEnum = field(default=EntityStatusEnum.NOT_LOADED)
    product: ProductEntity | EntityStatusEnum = field(default=EntityStatusEnum.NOT_LOADED)
    text: str = field(default='')
    rating: int = field(default=1)
