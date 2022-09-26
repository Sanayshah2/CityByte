from django.urls import path

from .views import city_suggestions

urlpatterns = [
    path('city', city_suggestions),
]
