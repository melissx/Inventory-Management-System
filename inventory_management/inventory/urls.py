from django.urls import path
from . import views

urlpatterns = [
  path('', views.product_list, name='product_list'),
  path('product/create/', views.product_create, name='product_create'),
  path('product/<int:pk>/update/', views.product_update, name='product_update'),
  path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
  path('product/<int:product_pk>/stock/', views.stock_update, name='stock_update'),
]
