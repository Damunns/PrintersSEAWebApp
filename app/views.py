"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Printer  # Import the Printer model

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
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    printers = Printer.objects.all()
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'This is a simple printer management system that allows you to view a list of printers. You can view the brand, model, location, IP address, MAC address, manufacture date, and comments for each printer. You can also add a new printer, edit an existing printer, or delete a printer. (Hi David - this was generated by copilot accdidentally and I thought it was worth keeping)',
            'year':datetime.now().year,
            'printers': printers,
        }
    )