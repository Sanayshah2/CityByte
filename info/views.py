from datetime import datetime

import pytz
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from info.helpers.places import FourSquarePlacesHelper
from info.helpers.weather import WeatherBitHelper
from search.helpers.photo import UnplashCityPhotoHelper

#multithreading. Static for now
def callfunc(category):
    city="pune"
    country="India"
    return (FourSquarePlacesHelper().get_places(city=f"{category[0]}, {category[1]}", categories=category[2], sort="RELEVANCE", limit=5))
 
pool = multiprocessing.Pool(processes = 4)
list=[[13065],[19040],[16000],[10000],[12013],[12082], [14000], [15000], [19000], [18000], [12000]]
results=pool.map(callfunc,list)

dining_info=results[0]
airport_info=results[1]
outdoor_info=results[2]
arts_info=results[3]
Education_info=results[4]
Organization_info=results[5]
Event_info=results[6]
Health_info=results[7]
Travel_info=results[8]
Sports=results[9]
Community = results[10]


@require_http_methods(["GET"])
def place_photo(request):
    photo_link = FourSquarePlacesHelper().get_place_photo(fsq_id=request.GET.get('fsq_id'))
    return redirect(photo_link)


@require_http_methods(["GET"])
def info_page(request):
    city = request.GET.get("city")
    country = request.GET.get("country")

    weather_info = WeatherBitHelper().get_city_weather(city=city, country=country)["data"][0]

    weather_info["sunrise"] = datetime.strptime(weather_info["sunrise"], "%H:%M").astimezone(
        pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
    weather_info["sunset"] = datetime.strptime(weather_info["sunset"], "%H:%M").astimezone(
        pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
    weather_info["ts"] = datetime.fromtimestamp(weather_info["ts"]).strftime("%m-%d-%Y, %H:%M")

    dining_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="13065", sort="RELEVANCE", limit=5)
    airport_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="19040", sort="RELEVANCE", limit=5)
    outdoor_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="16000", sort="RELEVANCE", limit=5)
    arts_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="10000", sort="RELEVANCE", limit=5)
    Education_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="12013", sort="RELEVANCE", limit=5)
 

    Organization_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="12082", sort="RELEVANCE", limit=5)
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)

    Event_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="14000", sort="RELEVANCE", limit=5)
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)

    Health_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="15000", sort="RELEVANCE", limit=5)
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
    
    Sports = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="18000", sort="RELEVANCE", limit=5)
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
    
    Travel_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="19000", sort="RELEVANCE", limit=5)
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
    
    Community = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="12000", sort="RELEVANCE", limit=5)
    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
    
    #All features done

    return render(
        request, 'search/city_info.html',
        context={
            "weather_info": weather_info,
            "dining_info": dining_info,
            "airport_info": airport_info,
            "outdoor_info": outdoor_info,
            "arts_info": arts_info,
            "photo_link": photo_link,
            'Education_info': Education_info,
            "Organization_info": Organization_info,
            "Event_info": Event_info,
            "Health_info": Health_info,
            "Travel_info": Travel_info,
            "Sports": Sports,
            "Community": Community
        }
    )
