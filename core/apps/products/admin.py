from django.contrib import admin

from core.apps.products.models.products import ProductModel
from core.apps.products.models.reviews import ReviewModel


class ReviewInline(admin.TabularInline):
    model = ReviewModel
    extra = 0


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_visible')
    inlines = (ReviewInline,)


@admin.register(ReviewModel)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'created_at', 'updated_at', 'rating')
    list_select_related = ('customer', 'product')
