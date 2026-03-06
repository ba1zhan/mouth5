from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Review, Category
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewListSerializer, CategoryListSerializer , CategoryDetailSerializer, ReviewDetailSerializer 
from rest_framework import status


@api_view(['GET', 'DELETE', 'PUT'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.rating = request.data.get('rating')
        product.price = request.data.get('price')
        product.category = request.data.get('category')
        product.save()
        return Response(data=ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.select_related('category').all()

        data = ProductListSerializer(product, many=True).data

        return Response(
            data=data,  
        )
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        rating = request.data.get('rating')
        price = request.data.get('price')

        product = Product.objects.create(
            title=title,
            description=description,
            rating=rating,
            price=price,
        )
        product.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)
    


@api_view(http_method_names=['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.select_related('product').all()

        data = ReviewListSerializer(review, many=True).data

        return Response(
            data=data,  
        )
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')

        review = Review.objects.create(
            text=text,
            stars=stars,
        )
        review.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewListSerializer(review).data)
    

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(review_detail, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review_detail.text = request.data.get('text')
        review_detail.stars = request.data.get('stars')
        review_detail.save()
        return Response(data=ReviewDetailSerializer(review_detail).data,
                        status=status.HTTP_201_CREATED)



@api_view(http_method_names=['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        data = CategoryListSerializer(category, many=True).data

        return Response(
            data=data,  
        )
    elif request.method == 'POST':
        name = request.data.get('name')

        category = Category.objects.create(
            name=name,
        )
        category.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryListSerializer(category).data)

@api_view(['GET', 'DELETE', 'PUT'])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'category not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = CategoryDetailSerializer(category_detail, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        category_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        category_detail.name = request.data.get('name')
        category_detail.save()
        return Response(data=CategoryDetailSerializer(category_detail).data,
                        status=status.HTTP_201_CREATED)
