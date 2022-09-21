from django.http import HttpRequest
from django.shortcuts import render

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Главная',
        }
    )
