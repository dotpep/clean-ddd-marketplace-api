r"""
1. Test products count: count with zero product, count with existing list of products
2. Test product returns all, w\ pagination test filters (title, description, no match)
"""
import pytest
from tests.factories.products import ProductModelFactory

from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService


@pytest.mark.django_db
def test_get_product_count_zero(product_service: BaseProductService):
    """Test products with count zero value of products in db."""
    products_count = product_service.get_product_count(filters=ProductFilters())
    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_get_product_count_exist(product_service: BaseProductService):
    EXPECTED_COUNT = 5
    ProductModelFactory.create_batch(size=EXPECTED_COUNT)

    products_count = product_service.get_product_count(filters=ProductFilters())
    assert products_count == EXPECTED_COUNT + 1, f"{products_count=} : {EXPECTED_COUNT=}"


@pytest.mark.skip(reason="not implemented")
def test_products_search():
    assert False
