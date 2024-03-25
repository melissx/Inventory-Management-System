from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=255, unique=True)
  description = models.TextField(blank=True)
  category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
  unit_price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

class Stock(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  reorder_level = models.PositiveIntegerField(blank=True, null=True)

  def __str__(self):
    return f"{self.product.name} ({self.quantity})"
