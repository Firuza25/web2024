from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products),
    path('products/<int:pk>', views.get_product_by_id),
    path('categories/', views.get_categories),
    path('categories/<int:pk>/', views.get_category_by_id),
    path('categories/<int:pk>/products', views.get_products_by_category),
 
]







    



