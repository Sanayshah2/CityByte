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
