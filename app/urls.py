from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('update_printers/', views.update_printers, name='update_printers'),
]