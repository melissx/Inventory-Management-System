from django import forms
from .models import Product, Stock

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'description', 'category', 'unit_price']

class StockForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['product', 'quantity', 'reorder_level']
