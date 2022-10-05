from abc import ABC, abstractmethod

from django.conf import settings

from search.utils.baseutils.search import SearchUtilBase
from search.utils.search import GeoDB
from search.utils.url import URL


class SearchAutoCompleteHelperBase(ABC):
    @abstractmethod
    def get_suggestions(self, city: str):
        pass


class GenericDBSearchAutoCompleteHelper(SearchAutoCompleteHelperBase):
    def __init__(self, klass: SearchUtilBase = None, url: URL = None):
        if url is None:
            klass = GeoDB
            url = URL(**settings.GEODB_CONFIG)

        self._search_util = klass(url=url)

    def get_suggestions(self, city: str, **kwargs):
        return self._search_util.get_city_suggestions(city=city, **kwargs)
