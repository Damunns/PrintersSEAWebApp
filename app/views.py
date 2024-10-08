"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponseBadRequest
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
            'message':'This is a simple printer management system that allows you to view all the printers on-site. You can view the brand, model, location, IP address, MAC address, manufacture date, and comments for each printer. You can also add a new printer, edit an existing printer, or delete a printer if you have the correct access.',
            'year':datetime.now().year,
            'printers': printers,
        }
    )

def update_printers(request,printer_id):
    printer = get_object_or_404(Printer, pk=printer_id)
    try:
        printer = Printer.objects.get(pk=printer_id)
    except (KeyError, printer.DoesNotExist):
        return render(request, 'app/about.html', {
            'printer': printer,
            'error_message': "Printer not found.",
        })
    else:
        brand = request.POST['brand']
        model = request.POST['model']
        location = request.POST['location']
        ip_address = request.POST['ip_address']
        mac_address = request.POST['mac_address']
        #print(datetime.strptime(request.POST['manufacture_date'], "%b. %d, %Y").strftime('%Y-%m-%d'))
        #print(datetime.strptime(request.POST['manufacture_date'], "%B %d, %Y").strftime('%Y-%m-%d'))
        try:
            manufacture_date = datetime.strptime(request.POST['manufacture_date'], "%B %d, %Y").strftime('%Y-%m-%d')
        except ValueError:
            try:
                manufacture_date = datetime.strptime(request.POST['manufacture_date'], '%b. %d, %Y').strftime('%Y-%m-%d')
            except ValueError:
                # Handle cases where the date format is invalid
                return HttpResponseBadRequest(f"Invalid date format - {request.POST['manufacture_date']}")
        comments = request.POST['comments']

        printer.brand = brand
        printer.model = model
        printer.location = location
        printer.ip_address = ip_address
        printer.mac_address = mac_address
        printer.manufacture_date = manufacture_date
        printer.comments = comments
        printer.save()
        return redirect('/about')
    



def add_printer(request,printer_id,printer_brand,printer_model,printer_location,printer_ip_address,printer_mac,printer_manufacture_date,printer_comments):
    printer = get_object_or_404(Printer, pk=printer_id)
    try:
        try:
            printer_id = request.POST['addRows']
            printer = Printer.objects.get(pk=printer_id)
        except ValueError:
            return render(request, 'app/about.html', {
                'printer': printer[printer_id],
                'error_message': "Invalid printer ID.",
            })
        print(printer.model)
    except (KeyError, printer.DoesNotExist):
        return render(request, 'app/about.html', {
            'printer': printer[printer_id],
            'error_message': "Printer not found.",
        })
    else:
        printer.brand = request.POST['brand-printer_id']
        printer.model = request.POST['model-printer_id']
        printer.location = request.POST['location-printer_id']
        printer.ip_address = request.POST['ip_address-printer_id']
        printer.mac_address = request.POST['mac_address-printer_id']
        printer.manufacture_date = request.POST['manufacture_date-printer_id']
        printer.comments = request.POST['comments-printer_id']
        printer.save()
