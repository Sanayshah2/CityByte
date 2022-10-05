from abc import ABC, abstractmethod

from django.conf import settings

from search.utils.photo import PhotoUtilBase
from search.utils.photo import Unsplash
from search.utils.url import URL


class CityPhotoHelperBase(ABC):
    @abstractmethod
    def get_city_photo(self, city: str):
        pass
