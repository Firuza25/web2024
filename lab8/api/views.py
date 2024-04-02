from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from .models import Product, Category

# def index(request):
# 	return HttpResponse("Hello, World! EMPTY PROJECT")

def get_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe = False)

def get_product_by_id(request, pk):
    product = Product.objects.get(id=pk)
    return JsonResponse(product.to_json())


def get_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe = False)

def get_category_by_id(request, pk):
    category = Category.objects.get(id=pk)
    return JsonResponse(category.to_json())

def get_products_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe = False)