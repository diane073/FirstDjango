from django.contrib import admin
from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'size', 'price',)


# Register your models here.
admin.site.register(ProductModel)
