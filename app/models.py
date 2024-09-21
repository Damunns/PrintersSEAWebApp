"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Printer(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)  # MAC addresses are typically 17 characters long
    manufacture_date = models.DateField()
    comments = models.TextField(blank=True, null=True)  # Allow comments to be optional

    def __str__(self):
        return f"{self.brand} {self.model} - {self.location}"