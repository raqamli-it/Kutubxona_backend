from django.urls import path

from .views import UserListView, UserDetailView, UserLoginView, UserLogoutView, UserRegisterView, UserUpdateView

app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('update/', UserUpdateView.as_view(), name='user-update'),
]