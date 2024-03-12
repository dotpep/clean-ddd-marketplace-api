from abc import ABC, abstractmethod
from typing import Iterable
# Protocol vs ABC

from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductModel  # Django ORM, Product DTO (Data Transfer Object)


class BaseProductService(ABC):  # Interface/Abstract (BaseNameService) IProductService
    @abstractmethod
    def get_product_list(self) -> Iterable[Product]:
        pass
    
    @abstractmethod
    def get_product_count(self) -> int:
        pass
    
    # abstractmethod decorator vs raise NotImplementedError()


class ORMProductService(BaseProductService):
    def get_product_list(self) -> Iterable[Product]:
        queryset = ProductModel.objects.filter(is_visible=True)
        return [
            product.to_entity() for product in queryset  # converter
        ]
    
    def get_product_count(self) -> int:
        return ProductModel.objects.filter(is_visible=True).count()
