from django.urls import path

from .views import BookListView, BookDetailView, LanguageFilterView, CategoryFilterView, SearchView, MagazineDetailView, \
    MagazineListView, DiscussDetailView, DiscussListView

app_name = 'books'
urlpatterns = [
    # Book
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('filter-language/', LanguageFilterView.as_view(), name='filter-language'),
    path('filter-category/', CategoryFilterView.as_view(), name='filter-category'),
    path('search/', SearchView.as_view(), name='book-search'),
    # Discuss
    path('discuss-list/', DiscussListView.as_view(), name='discuss-list'),
    path('discuss-detail/', DiscussDetailView.as_view(), name='discuss-detail'),
    # Magazine
    path('magazine-list/', MagazineListView.as_view(), name='magazine-list'),
    path('magazine-detail/<int:pk>/', MagazineDetailView.as_view(), name='magazine-detail'),
]
