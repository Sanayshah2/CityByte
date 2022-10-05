from django.urls import path

from .views import city_suggestions, city_photo

urlpatterns = [
    path('city', city_suggestions),
    path('city/photo', city_photo),
]
