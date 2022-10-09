from abc import ABC, abstractmethod

from django.conf import settings

from search.utils.photo import PhotoUtilBase
from search.utils.photo import Unsplash
from search.utils.url import URL


class CityPhotoHelperBase(ABC):
    @abstractmethod
    def get_city_photo(self, city: str):
        pass


class UnplashCityPhotoHelper(CityPhotoHelperBase):
    def __init__(self, klass: PhotoUtilBase = None, url: URL = None):
        if url is None:
            klass = Unsplash
            url = URL(**settings.UNSPLASH_CONFIG)

        self._photo_util = klass(url=url)

    def get_city_photo(self, city: str):
        photo_list = self._photo_util.get_photos(query=city)

        if len(photo_list) == 0:
            return None

        return photo_list[1]["urls"]["regular"]
