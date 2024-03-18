import factory
from factory.django import DjangoModelFactory

from core.apps.products.models.products import ProductModel


class ProductModelFactory(DjangoModelFactory):
    title = factory.Faker('first_name')
    description = factory.Faker('text', max_nb_chars=255)

    class Meta:
        model = ProductModel
