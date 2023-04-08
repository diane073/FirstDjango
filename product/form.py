from .models import ProductModel
from django import forms

# form


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['code',
                  'name',
                  'description',
                  'price',
                  'size']
