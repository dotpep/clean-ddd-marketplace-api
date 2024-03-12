from django.urls import path
from ninja import NinjaAPI
from django.http import HttpRequest

from core.api.schemas import PingResponseSchema
from core.api.v1.urls import router as v1_router


api = NinjaAPI()


api.add_router('v1/', v1_router)

urlpatterns = [
    path("", api.urls),
]


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    #return {"result": True}
    return PingResponseSchema(result=True)

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
