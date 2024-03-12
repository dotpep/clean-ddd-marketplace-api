from ninja import Router
from django.http import HttpRequest

from core.api.v1.products.schemas import ProductListSchema, ProductSchema
from core.apps.products.services.products import BaseProductService, ORMProductService


router = Router(tags=['Products'])


@router.get('', response=ProductListSchema)
def get_product_list_handler(request: HttpRequest) -> ProductListSchema:
    # without dependency injection
    service: BaseProductService = ORMProductService()
    product_list = service.get_product_list()
    
    return [
        ProductSchema.from_entity(obj) for obj in product_list  # converter
    ]
