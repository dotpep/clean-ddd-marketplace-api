from pydantic import BaseModel

from datetime import datetime
from typing import List

from core.apps.products.entities.products import Product as ProductEntity


class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None
    
    # simplified converter
    @staticmethod
    def from_entity(entity: ProductEntity) -> 'ProductSchema':  # (from __future__ import annotations)
        return ProductSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )


ProductListSchema = list[ProductSchema]
