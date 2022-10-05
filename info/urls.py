from django.urls import path

from search.views import place_photo

urlpatterns = [
    path('place/photo', place_photo, name="place_photo"),
]
