r"""
1. Test products count: count with zero product, count with existing list of products
2. Test product returns all, w\ pagination test filters (title, description, no match)
"""
import pytest
from tests.factories.products import ProductModelFactory

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService


@pytest.mark.django_db
def test_get_product_count_zero(product_service: BaseProductService):
    """Test products with count of zero in test_django_db."""
    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_get_product_count_exist(product_service: BaseProductService):
    """Test products with count of existing model data EXPECTED_COUNT = 5 in
    test_django_db using factory_boy, faker."""
    EXPECTED_COUNT = 5
    ProductModelFactory.create_batch(size=EXPECTED_COUNT)

    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == EXPECTED_COUNT, f"{products_count=} == {EXPECTED_COUNT=}"


@pytest.mark.django_db
def test_get_product_list(product_service: BaseProductService):
    EXPECTED_COUNT = 5
    products = ProductModelFactory.create_batch(size=EXPECTED_COUNT)
    products_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    fetched_titles = {product.title for product in fetched_products}
    fetched_titles_length = len(fetched_titles)

    assert fetched_titles_length == EXPECTED_COUNT, f"{fetched_titles_length=} == {EXPECTED_COUNT=}"
    assert fetched_titles == products_titles, f"{fetched_titles=} == {products_titles=}"


@pytest.mark.skip(reason="not implemented")
def test_products_search():
    assert False
