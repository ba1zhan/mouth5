from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Review, Category
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewListSerializer, CategoryListSerializer  
from rest_framework import status


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    products = Product.objects.all()

    data = ProductListSerializer(products, many=True).data

    return Response(
        data=data,  
    )

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()

    data = ReviewListSerializer(reviews, many=True).data

    return Response(
        data=data,  
    )

@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()

    data = CategoryListSerializer(categories, many=True).data

    return Response(
        data=data,  
    )