from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView

from books.models import Book, Author
from books.serializers import BookListSerializer, AuthorListSerializer


# Book
# class BookListView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookCreateView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookDetailView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookUpdateView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookDeleteView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# # Author
# class AuthorListView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer
#
#
# class AuthorCreateView(CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer
#
#
# class AuthorDetailView(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer
#
#
# class AuthorUpdateView(UpdateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer
#
#
# class AuthorDeleteView(DestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
