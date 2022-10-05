from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from search.helpers.autocomplete import GenericDBSearchAutoCompleteHelper

@require_http_methods(["GET"])
def main_page(request):
    return render(request, 'search/search.html')

@require_http_methods(["GET"])
def city_suggestions(request):
    suggestions_data = GenericDBSearchAutoCompleteHelper(
        klass=AmadeusCitySearch, url=URL(**settings.AMADEUS_CONFIG)
    ).get_suggestions(city=request.GET.get("q"), max=10)
    
    return JsonResponse({
        "results": suggestions_data.get("data", [])
    })
