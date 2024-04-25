# base.model --> .json

from rest_framework import serializers
from .models import Book, Author


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id', 'title', 'author', 'image', 'price', 'published_date']


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['id', 'full_name', 'birth_date']
