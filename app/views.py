"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest, HttpResponseBadRequest
from .models import Printer  # Import the Printer model
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .forms import BootstrapAuthenticationForm, BootstrapUserCreationForm
from dateutil import parser
from django.core.exceptions import PermissionDenied
from django.contrib import messages

def login(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Landing Page',
            'year':datetime.now().year,
        }
    )
@login_required
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
def register(request):
    """Renders the register page and handles user registration."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/about')
    else:
        form = BootstrapUserCreationForm()
    return render(
        request,
        'app/register.html',
        {
            'title':'Register',
            'year':datetime.now().year,
            'form': form,
        }
    )

def update_printer(request,printer_id):
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
        try:
            manufacture_date = parser.parse(request.POST['manufacture_date']).date()
        except (ValueError, TypeError):
            return HttpResponseBadRequest(f"Invalid date format - {request.POST['manufacture_date']}")
        comments = request.POST['comments']
        
        printer.editPrinter(id=printer_id, brand=brand, model=model, location=location, ip_address=ip_address, mac_address=mac_address, manufacture_date=manufacture_date, comments=comments)

        return redirect('/about')

def add_printer(request):
    try:
        manufacture_date = parser.parse(request.POST['manufacture_date']).date()
        manufacture_date_str = manufacture_date.strftime('%Y-%m-%d')  # Convert to string
    except (ValueError, TypeError):
        return HttpResponseBadRequest(f"Invalid date format - {request.POST['manufacture_date']}")
    printer = Printer(
        brand=request.POST['brand'],
        model=request.POST['model'],
        location=request.POST['location'],
        ip_address=request.POST['ip_address'],
        mac_address=request.POST['mac_address'],
        manufacture_date=manufacture_date_str,
        comments=request.POST['comments']
    )
    printer.save()
    return redirect('/about')

def delete_printer(request, printer_id):
    # Manually check if the user has the required permission
    if not request.user.has_perm('app.delete_printer'):
        # Set a flash message for lack of permissions
        messages.error(request, "You do not have the required permissions to delete this printer.")
        return redirect('/about')  # Redirect to a safe page (e.g., the "about" page)

    printer = get_object_or_404(Printer, pk=printer_id)
    printer.delete()
    messages.success(request, "Printer deleted successfully.")
    return redirect('/about')