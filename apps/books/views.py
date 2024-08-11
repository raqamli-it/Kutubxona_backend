from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Book, Category, Language, Discuss, Magazine


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'books/book-list.html', context)


class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        context = {'book': book}
        return render(request, 'books/book-detail.html', context)


class CategoryFilterView(View):
    def get_queryset(self):
        categories = Category.objects.all()
        queryset = Book.objects.filter(category=self.request.GET.getlist('category'))
        return queryset

    # def get(self):
    #     books = Book.objects.filter(category_id=self.kwargs['category_id'])
    #     return books


class LanguageFilterView(View):
    def get_queryset(self):
        languages = Language.objects.all()
        queryset = Language.objects.filter(language=self.request.GET.getlist('language'))
        return queryset

    # def get(self):
    #     books = Book.objects.filter(language_id=self.request.GET.getlist('language_id'))
    #     return books


class SearchView(ListView):
    template_name = 'books/book-list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class DiscussListView(View):
    def get(self, request):
        discusses = Discuss.objects.all()
        context = {'discusses': discusses}
        return render(request, 'books/discuss-list.html', context)


class DiscussDetailView(View):
    def get(self, request, book_id):
        discuss = Discuss.objects.get(pk=book_id)
        context = {'discuss': discuss}
        return render(request, 'books/discuss-detail.html', context)


class MagazineListView(View):
    def get(self, request):
        magazines = Magazine.objects.all()
        context = {'magazines': magazines}
        return render(request, 'books/magazine-list.html', context)


class MagazineDetailView(View):
    def get(self, request, book_id):
        magazine = Magazine.objects.get(pk=book_id)
        context = {'magazine': magazine}
        return render(request, 'books/magazine-detail.html', context)
