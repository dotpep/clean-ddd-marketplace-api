from functools import lru_cache

import punq

from core.apps.products.services.products import (
    BaseProductService,
    ORMProductService,
)


@lru_cache
def get_container() -> punq.Container:
    """Dependency injection container for service."""
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()
    container.register(BaseProductService, ORMProductService)

    return container
