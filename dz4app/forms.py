from django import forms
from dz4app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'description', 'price', 'quantity', 'photo']