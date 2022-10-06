

def test_info_page(request):
    city = 'New York City'
    country = 'US'
    weather_info = WeatherBitHelper().get_city_weather(city=city, country=country)["data"][0]
    # print('weather_info',weather_info)

    weather_info["sunrise"] = datetime.strptime(weather_info["sunrise"], "%H:%M").astimezone(pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
    weather_info["sunset"] = datetime.strptime(weather_info["sunset"], "%H:%M").astimezone(pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
    weather_info["ts"] = datetime.fromtimestamp(weather_info["ts"]).strftime("%m-%d-%Y, %H:%M")


    dining_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="13065", sort="RELEVANCE", limit=5)
    outdoor_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="16000", sort="RELEVANCE", limit=5)
    airport_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="19040", sort="RELEVANCE", limit=5)
    arts_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="10000", sort="RELEVANCE", limit=5)

    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)

    assert render(request, 'search/city_info.html',context={
            "weather_info": weather_info,
            "dining_info": dining_info,
            "outdoor_info": outdoor_info,
            "airport_info": airport_info,
            "photo_link": photo_link,
            "arts_info": arts_info,
        }).status_code ==200  