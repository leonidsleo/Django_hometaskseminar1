from django import forms
from .models import Product


class ProductForm(forms.Form):
    name_product = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField()
