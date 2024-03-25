from django.apps import AppConfig

from core.apps.products.containers import ProductContainer


container = ProductContainer()


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.products'
    verbose_name = 'Product'
