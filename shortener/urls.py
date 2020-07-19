from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, re_path
from shortener.views import UrlListViewSet, UrlShortener, UrlExport

router = DefaultRouter()
router.register('', UrlListViewSet)

urlpatterns = [
    re_path(r'^shortener/(?P<origin_uri>.+)$', UrlShortener.as_view()),
    path('export/', UrlExport.as_view()),
]

urlpatterns += router.urls