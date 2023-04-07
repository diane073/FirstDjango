from django.contrib import admin
from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


# Register your models here.
admin.site.register(ProductModel)
