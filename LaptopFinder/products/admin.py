from django.contrib import admin
from .models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price', 'type', 'photo', 'brand_name')
    list_filter = ('product_name', 'type',)
    search_fields = ('product_name', 'type',)


admin.site.register(Product, ProductAdmin)
