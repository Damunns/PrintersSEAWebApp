from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('update_printers/<printer_id>/', views.update_printers, name='update_printers'),
]