from django.contrib import admin
from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'size', 'created_at']


admin.site.register(ProductModel, ProductAdmin)
