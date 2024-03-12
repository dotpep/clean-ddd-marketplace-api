from pydantic import BaseModel, Field

from typing import Any, Generic, TypeVar


TData = TypeVar('TData')
TListItem = TypeVar('TListItem')


class PingResponseSchema(BaseModel):
    result: bool = False


class PaginationOut(BaseModel):
    offset: int
    limit: int
    total: int


class ListPaginatedResponse(BaseModel, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(BaseModel, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)
