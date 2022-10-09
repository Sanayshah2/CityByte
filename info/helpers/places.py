from abc import ABC, abstractmethod

from django.conf import settings

from info.utils.places import PlacesUtilBase, FourSquare
from search.utils.url import URL


class CityPlacesHelperBase(ABC):
    @abstractmethod
    def get_places(self, city: str, **kwargs):
        pass


class FourSquarePlacesHelper(CityPlacesHelperBase):
    def __init__(self, klass: PlacesUtilBase = None, url: URL = None):
        if url is None:
            klass = FourSquare
            url = URL(**settings.FOURSQUARE_CONFIG)

        self._places_util = klass(url=url)

    def get_places(self, city: str, **kwargs):
        return self._places_util.get_places(city=city, **kwargs)

    def get_place_photo(self, fsq_id: str):
        return self._places_util.get_place_photo(fsq_id=fsq_id)
