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
    manufacture_date = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)  # Allow comments to be optional

    def __str__(self):
        return f"{self.brand} {self.model} - {self.location}"
    
    def addPrinter(self, brand, model, location, ip_address, mac_address, manufacture_date, comments):
        new_printer = Printer(brand=brand, model=model, location=location, ip_address=ip_address, mac_address=mac_address, manufacture_date=manufacture_date, comments=comments)
        new_printer.save()
        return new_printer
    
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

    def deletePrinter(self, id):
        printer = Printer.objects.get(id=id)
        printer.delete()
        return None