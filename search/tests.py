from urllib import request
from django.test import TestCase
from info.helpers.places import FourSquarePlacesHelper
from search import views
import pytest
from search.helpers.autocomplete import GenericDBSearchAutoCompleteHelper
from django.shortcuts import render, redirect
from info.helpers.weather import WeatherBitHelper
from datetime import datetime
import pytz
from pytz import timezone
from search.helpers.photo import UnplashCityPhotoHelper
from search.utils.search import AmadeusCitySearch
from urllib.request import urlopen
image_formats = ("image/png", "image/jpeg", "image/gif")

class CityByte_testcase(TestCase):
  def test_main_page(self):
      #print('hiiiii',render(request, 'search/search.html').status_code,'byeeee')
      assert (render(request, 'search/search.html').status_code ==200)
      #return render(request, 'search/search.html')
