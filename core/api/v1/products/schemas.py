from pydantic import BaseModel

from datetime import datetime
from typing import List


class ProductSchema(BaseModel):
    title: str
    description: str
    is_visible: bool
    created_at: datetime
    updated_at: datetime | None = None


class ProductListSchema(BaseModel):
    products: List[ProductSchema]
