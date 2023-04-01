from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Product
from api.models import Category
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe = False)

def get_product_by_id(request,product_id):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    for product in products_json:
        if product['id'] == product_id:
            return JsonResponse(product)
    return JsonResponse({'error' : 'Product not found'})

def category_list(request):
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]
    return JsonResponse(categories_json, safe = False)

def get_category_by_id(request,category_id):
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]
    for category in categories_json:
        if category['id'] == category_id:
            return JsonResponse(category)
    return JsonResponse({'error' : 'Category not found'})
    

def product_list_by_category(request,category_id):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]
    r_products = []
    for category in categories_json:
        if category['id'] == category_id:
            for product in products_json:
                if category['name'] == product['name']:
                    r_products.append(product)  
    return JsonResponse(r_products, safe = False)
