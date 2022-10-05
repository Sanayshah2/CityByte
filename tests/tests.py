from info.helpers.places import FourSquarePlacesHelper
from django.test import TestCase
from urllib.request import urlopen
image_formats = ("image/png", "image/jpeg", "image/gif")

def test_photo():
    photo_link = FourSquarePlacesHelper().get_place_photo(fsq_id='518a71ab498e430858000827')
    #assert photo_link == 'https://fastly.4sqi.net/img/general/250x250/33256190_KwhKlZ90963X-l1Vzda668M0CFO1Lxujlg2TIsySBfM.jpg'
    site = urlopen(photo_link)
    meta = site.info()  
    if meta["content-type"] in image_formats: 
        assert True
