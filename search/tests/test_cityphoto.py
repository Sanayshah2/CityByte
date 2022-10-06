from search.helpers.photo import UnplashCityPhotoHelper
from django.test import TestCase
from urllib.request import urlopen
image_formats = ("image/png", "image/jpeg", "image/gif")

def test_cityphoto():
    photo_link = UnplashCityPhotoHelper().get_city_photo(city='Pune')
    site = urlopen(photo_link)
    meta = site.info() 
    if meta["content-type"] in image_formats: 
        assert True
