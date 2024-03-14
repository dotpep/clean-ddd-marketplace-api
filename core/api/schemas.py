from pydantic import Field
from ninja import Schema

from typing import Any, Generic, TypeVar

from core.api.filters import PaginationOut


TData = TypeVar('TData')
TListItem = TypeVar('TListItem')


class PingResponseSchema(Schema):
    is_healthy: bool = False


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)
