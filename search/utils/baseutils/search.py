from abc import ABC, abstractmethod

from search.utils.url import URL


class SearchUtilBase(ABC):
    _url: URL = None

    def __init__(self, url: URL):
        self._url = url

    @abstractmethod
    def get_city_suggestions(self, city: str, **kwargs):
        pass
