from abc import ABC, abstractmethod

from django.conf import settings

from info.utils.weather import WeatherBit, WeatherUtilBase
from search.utils.url import URL


class CityWeatherHelperBase(ABC):
    @abstractmethod
    def get_city_weather(self, city: str, **kwargs):
        pass