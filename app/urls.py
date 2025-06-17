from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('update_printer/<printer_id>/', views.update_printer, name='update_printer'),
    path('add_printer/', views.add_printer, name='add_printer'),
    path('delete_printer/<printer_id>/', views.delete_printer, name='delete_printer'),
]