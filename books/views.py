from django.shortcuts import render
from rest_framework.generics import ListAPIView

from books.models import Book
from books.serializers import BookListSerializer


# Create your views here.
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

