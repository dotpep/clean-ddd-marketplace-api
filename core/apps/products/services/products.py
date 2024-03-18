from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.entities.products import ProductEntity
from core.apps.products.models.products import ProductModel  # Django ORM, Product DTO (Data Transfer Object)


# Protocol vs ABC
class BaseProductService(ABC):  # Interface/Abstract (BaseNameService) IProductService
    @abstractmethod
    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        pass

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int:
        pass


# TODO: implement filters to service layer for avoid violating D principles in SOLID
class ORMProductService(BaseProductService):
    def _build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )

        return query

    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        query = self._build_product_query(filters)

        pagination_offset = pagination.offset
        pagination_step = pagination_offset + pagination.limit

        # product pagination using python slicing
        queryset = ProductModel.objects.filter(query)[pagination_offset:pagination_step]
        return [
            # TODO: Implement correct DDD separated fucntion converter for converting Domain Entity ORM/Etc(DTO), Schema
            product.to_entity()
            for product in queryset
        ]

    def get_product_count(self, filters: ProductFilters) -> int:
        query = self._build_product_query(filters)

        return ProductModel.objects.filter(query).count()
