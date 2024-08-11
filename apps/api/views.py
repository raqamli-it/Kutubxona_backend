from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from apps.api.serializers import BookSerializer, DiscussSerializer, MagazineSerializer, AbstractSerializer
from apps.books.models import Book, Abstract, Discuss, Magazine

from apps.users.models import User
from .serializers import UserSerializer


class AbstractAPIPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = AbstractAPIPagination


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = AbstractAPIPagination


class DiscussAPIViewSet(viewsets.ModelViewSet):
    queryset = Discuss.objects.all()
    serializer_class = DiscussSerializer


class MagazineAPIViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    pagination_class = AbstractAPIPagination


class AbstractAPIViewSet(viewsets.ModelViewSet):
    queryset = Abstract.objects.all()
    serializer_class = AbstractSerializer
    pagination_class = AbstractAPIPagination
