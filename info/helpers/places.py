from abc import ABC, abstractmethod

from django.conf import settings

from info.utils.places import PlacesUtilBase, FourSquare
from search.utils.url import URL


class CityPlacesHelperBase(ABC):
    @abstractmethod
    def get_places(self, city: str, **kwargs):
        pass
