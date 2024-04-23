# base.model --> .json

from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id', 'title', 'author', 'image', 'price', 'published_date']
