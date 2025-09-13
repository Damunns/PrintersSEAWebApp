"""
Definition of models.
"""
from django.db import models

# Create your models here.
class Printer(models.Model):
    #id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100, blank=False, null=False, default="Brand")
    model = models.CharField(max_length=100, blank=False, null=False, default="Model")
    location = models.CharField(max_length=255, blank=False, null=False, default="Location")
    ip_address = models.GenericIPAddressField(blank=False, null=False, default="0.0.0.0")
    mac_address = models.CharField(max_length=17, blank=False, null=False, default="00:00:00:00:00:00")  # MAC addresses are typically 17 characters long
    manufacture_date = models.CharField(max_length=100, blank=False, null=False, default="1900-00-00")
    comments = models.TextField(blank=True, null=True, default="Comments")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.location}"
    
    def editPrinter(self, id, brand, model, location, ip_address, mac_address, manufacture_date, comments):
        printer = Printer.objects.get(id=id)
        printer.brand = brand
        printer.model = model
        printer.location = location
        printer.ip_address = ip_address
        printer.mac_address = mac_address
        printer.manufacture_date = manufacture_date
        printer.comments = comments
        printer.save()
        return printer