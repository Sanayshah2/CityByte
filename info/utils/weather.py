from abc import ABC, abstractmethod

import requests

from search.utils.url import URL


class WeatherUtilBase(ABC):
    _url: URL = None

    def __init__(self, url: URL):
        self._url = url

    @abstractmethod
    def get_city_weather(self, city: str, **kwargs):
        pass


class WeatherBit(WeatherUtilBase):
    def get_city_weather(self, city: str, **kwargs):
        params = self._url.with_default_params({"city": city})
        

        response = requests.request(
            "GET", str(self._url.get_url(path="/current")),
            
            params=params,
        )

        return response.json()