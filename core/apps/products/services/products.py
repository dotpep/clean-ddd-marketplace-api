from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.apps.products.entities.products import ProductEntity
from core.apps.products.exceptions.products import ProductNotFoundException
from core.apps.products.filters.products import ProductFiltersEntity
from core.apps.products.models.products import ProductModel  # Django ORM, Product DTO (Data Transfer Object)


# Protocol vs ABC
class BaseProductService(ABC):  # Interface/Abstract (BaseNameService) IProductService
    @abstractmethod
    def get_product_list(
        self,
        filters: ProductFiltersEntity,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        pass

    @abstractmethod
    def get_product_count(self, filters: ProductFiltersEntity) -> int:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> int:
        pass


# Service and Repository layers is implemented by one in service layer
class ORMProductService(BaseProductService):
    def _build_product_query(self, filters: ProductFiltersEntity) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )

        return query

    def get_product_list(
        self,
        filters: ProductFiltersEntity,
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

    def get_product_count(self, filters: ProductFiltersEntity) -> int:
        query = self._build_product_query(filters)

        return ProductModel.objects.filter(query).count()

    def get_by_id(self, product_id: int) -> int:
        try:
            product_dto = ProductModel.objects.get(pk=product_id)
        except ProductModel.DoesNotExist:
            raise ProductNotFoundException(product_id=product_id)

        return product_dto.to_entity()
