from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from search.helpers.autocomplete import GenericDBSearchAutoCompleteHelper
from search.helpers.photo import UnplashCityPhotoHelper
from info.helpers.places import FourSquarePlacesHelper

@require_http_methods(["GET"])
def main_page(request):
    return render(request, 'search/search.html')

@require_http_methods(["GET"])
def city_suggestions(request):
    suggestions_data = GenericDBSearchAutoCompleteHelper(
        klass=AmadeusCitySearch, url=URL(**settings.AMADEUS_CONFIG)
    ).get_suggestions(city=request.GET.get("q"), max=10)
    
    return JsonResponse({
        "results": suggestions_data.get("data", [])
    })

@require_http_methods(["GET"])
def city_photo(request):
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=request.GET.get("q"))
    return JsonResponse({
        "path": photo_link
    })
@require_http_methods(["GET"])
def place_photo(request):
    photo_link = FourSquarePlacesHelper().get_place_photo(fsq_id=request.GET.get('fsq_id'))
    # print("**************",request.GET.get('fsq_id'))
    # print("...........",photo_link)
    return redirect(photo_link)