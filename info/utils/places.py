from abc import ABC, abstractmethod

import requests

from search.utils.url import URL


class PlacesUtilBase(ABC):
    _url: URL = None

    def __init__(self, url: URL):
        self._url = url

    @abstractmethod
    def get_places(self, city: str, **kwargs):
        pass
    
class FourSquare(PlacesUtilBase):
    def get_places(self, city: str, **kwargs):
        params = self._url.with_default_params({"near": city})
        params.update(kwargs)

        response = requests.request(
            "GET", str(self._url.get_url(path="/v3/places/search")),
            headers=self._url.with_default_headers(),
            params=params
        )

        return response.json()
