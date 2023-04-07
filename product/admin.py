from django.contrib import admin
from .models import ProductModel


# Register your models here.
admin.site.register(ProductModel)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'size', 'price')
