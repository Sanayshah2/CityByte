from abc import ABC, abstractmethod

import requests
from django.conf import settings

from search.utils.url import URL

class SearchUtilBase(ABC):
    _url: URL = None

    def __init__(self, url: URL):
        self._url = url

    @abstractmethod
    def get_city_suggestions(self, city: str, **kwargs):
        pass


class GeoDB(SearchUtilBase):
    def get_city_suggestions(self, city: str, **kwargs):
        offset = kwargs.get("offset", 0)
        limit = kwargs.get("limit", 10)

        response = requests.request(
            "GET", str(self._url.get_url(path="/v1/geo/cities")),
            headers=self._url.with_default_headers(),
            params=self._url.with_default_headers({"namePrefix": city, "offset": offset, "limit": limit})
        )

        return response.json()
