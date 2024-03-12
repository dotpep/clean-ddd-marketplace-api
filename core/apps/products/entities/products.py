from dataclasses import dataclass

import datetime


# Domain Entity (simplified DDD without object value and validation) for retrive DTO
@dataclass
class Product:
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
