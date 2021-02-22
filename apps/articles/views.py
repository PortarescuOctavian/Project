from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Comment
from rest_framework import viewsets
from .serializers import ProductSerializer, CommentSerializer


class ProductList(APIView):

    def get(self, request):
        stocks = Product.objects.all()
        serializer = ProductSerializer(stocks, many=True)
        return Response(serializer.data)


class CommentList(APIView):

    def get(self, request):
        stocks = Comment.objects.all()
        serializer = CommentSerializer(stocks, many=True)
        return Response(serializer.data)
