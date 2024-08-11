from rest_framework import serializers

from apps.books.models import Book, Discuss, Magazine, Abstract

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'category_name', 'language_name', 'scan')


class DiscussSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)

    class Meta:
        model = Discuss
        fields = ('title', 'category_name', 'language_name')


class MagazineSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)

    class Meta:
        model = Magazine
        fields = ('title', 'category_name', 'language_name')


class AbstractSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)

    class Meta:
        model = Abstract
        fields = ('title', 'category_name', 'language_name')
