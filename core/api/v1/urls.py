from django.http import HttpRequest
from ninja import Router

from core.api.schemas import PingResponseSchema
from core.api.v1.products.handlers import router as product_router


router = Router()

router.add_router('products/', product_router)


@router.get("/ping", tags=['Check Health'], response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(is_healthy=True)
