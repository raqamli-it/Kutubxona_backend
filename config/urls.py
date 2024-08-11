"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.api.views import BookAPIViewSet, DiscussAPIViewSet, MagazineAPIViewSet, AbstractAPIViewSet
from config import settings

from apps.api.views import UserAPIViewSet
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'users', UserAPIViewSet, basename='users')
router.register(r'books', BookAPIViewSet, basename='books')
router.register(r'discusses', DiscussAPIViewSet, basename='discusses')
router.register(r'magazines', MagazineAPIViewSet, basename='magazines')
router.register(r'abstracts', AbstractAPIViewSet, basename='abstracts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include('apps.books.urls')),
    path('users/', include('apps.users.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
