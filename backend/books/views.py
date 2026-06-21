from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Category
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer


BOOKS_LIST_CACHE_KEY = "books_list"


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(BOOKS_LIST_CACHE_KEY)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(BOOKS_LIST_CACHE_KEY, response.data, timeout=60)

        return response

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.delete(BOOKS_LIST_CACHE_KEY)
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(BOOKS_LIST_CACHE_KEY)
        return instance

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete(BOOKS_LIST_CACHE_KEY)
