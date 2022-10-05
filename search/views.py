from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from info.helpers.weather import WeatherBitHelper
from search.helpers.autocomplete import GenericDBSearchAutoCompleteHelper
from search.helpers.photo import UnplashCityPhotoHelper
from info.helpers.places import FourSquarePlacesHelper
from search.utils.search import AmadeusCitySearch
from search.utils.url import URL


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
    return redirect(photo_link)


@require_http_methods(["GET"])
def info_page(request):
    city = request.GET.get("city")
    country = request.GET.get("country")

    weather_info = WeatherBitHelper().get_city_weather(city=city, country=country)["data"][0]

    dining_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="13065", sort="RELEVANCE", limit=5)
    airport_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="19040", sort="RELEVANCE", limit=5)

    return render(
        request, 'search/city_info.html',
        context={
            "weather_info": weather_info,
            "dining_info": dining_info,
            "airport_info": airport_info,
        }
    )
