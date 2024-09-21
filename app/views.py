"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def brief(request):
    """Renders the brief page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/brief.html',
        {
            'title':'Assignment Brief',
            'year':datetime.now().year,
        }
    )
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'This is my application description page.',
            'year':datetime.now().year,
        }
    )