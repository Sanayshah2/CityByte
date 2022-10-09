from abc import ABC, abstractmethod

from django.conf import settings

from info.utils.weather import WeatherBit, WeatherUtilBase
from search.utils.url import URL


class CityWeatherHelperBase(ABC):
    @abstractmethod
    def get_city_weather(self, city: str, **kwargs):
        pass


class WeatherBitHelper(CityWeatherHelperBase):
    def __init__(self, klass: WeatherUtilBase = None, url: URL = None):
        if url is None:
            klass = WeatherBit
            url = URL(**settings.WEATHER_BIT_CONFIG)

        self._weather_util = klass(url=url)

    def get_city_weather(self, city: str, **kwargs):
        return self._weather_util.get_city_weather(city=city, **kwargs)
