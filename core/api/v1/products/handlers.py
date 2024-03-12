from ninja import Router, Query
from django.http import HttpRequest

from core.api.v1.products.schemas import ProductSchema
from core.apps.products.services.products import BaseProductService, ORMProductService

from core.api.schemas import ApiResponse, ListPaginatedResponse
from core.api.filters import PaginationIn, PaginationOut
from core.api.v1.products.filters import ProductFilters


router = Router(tags=['Products'])


@router.get('', response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_product_list_handler(
    request: HttpRequest, 
    # Query parameters
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn]
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    # without dependency injection
    service: BaseProductService = ORMProductService()
    product_list = service.get_product_list(filters=filters, pagination=pagination_in)
    product_count = service.get_product_count(filters=filters)
    
    items = [ProductSchema.from_entity(obj) for obj in product_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset, 
        limit=pagination_in.limit, 
        total=product_count
    )
    
    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination_out))
