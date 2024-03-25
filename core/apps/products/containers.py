"""Dependency injection container for product."""
from dependency_injector import (
    containers,
    providers,
)

from core.apps.products.services.products import ORMProductService


class ProductContainer(containers.DeclarativeContainer):
    # Fabricates a product using Factory pattern in providers (providers.Factory())
    # Using Singleton pattern (providers.Singleton())
    product_service = providers.Singleton(ORMProductService)
