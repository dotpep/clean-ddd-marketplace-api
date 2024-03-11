from django.urls import path
from ninja import NinjaAPI
from django.http import HttpRequest

from core.api.schemas import PingResponseSchema


api = NinjaAPI()

@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    #return {"result": True}
    return PingResponseSchema(result=True)

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


urlpatterns = [
    path("v1/", api.urls),
]
