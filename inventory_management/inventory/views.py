from django.shortcuts import render, redirect
from .models import Product, Stock
from .forms import ProductForm, StockForm

def product_list(request):
  products = Product.objects.all()
  context = {'products': products}
  return render(request, 'inventory/product_list.html', context)

def product_create(request):
  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('product_list')  # Redirect to product list after successful creation
  else:
    form = ProductForm()
  context = {'form': form}
  return render(request, 'inventory/product_form.html', context)

def product_update(request, pk):
  product = Product.objects.get(pk=pk)
  if request.method == 'POST':
    form = ProductForm(request.POST, instance=product)  # Update existing product instance
    if form.is_valid():
      form.save()
      return redirect('product_list')  # Redirect to product list after successful update
  else:
    form = ProductForm(instance=product)  # Pre-populate form with existing product data
  context = {'form': form}
  return render(request, 'inventory/product_form.html', context)

def product_delete(request, pk):
  product = Product.objects.get(pk=pk)
  if request.method == 'POST':
    product.delete()
    return redirect('product_list')  # Redirect to product list after deletion
  context = {'product': product}
  return render(request, 'inventory/product_delete.confirm.html', context)

def stock_update(request, product_pk):
  product = Product.objects.get(pk=product_pk)
  stock, created = Stock.objects.get_or_create(product=product)  # Get or create stock record for the product
  if request.method == 'POST':
    form = StockForm(request.POST, instance=stock)  # Update existing stock instance
    if form.is_valid():
      form.save()
      return redirect('product_list')  # Redirect to product list after successful update
  else:
    form = StockForm(instance=stock)  # Pre-populate form with existing stock data
  context = {'form': form, 'product': product}
  return render(request, 'inventory/stock_form.html', context)
