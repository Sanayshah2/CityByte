from django.shortcuts import render, redirect
import pytest

def test_main_page(request):
    assert (render(request, 'search/search.html').status_code ==200)
