from django.db import models

# Create your models here.

PROPERTY_STATUS  = [
    ("RENT", "rent"),
    ("SALE", "sale")
]

PROPERTY_TYPE = [
    ("Apartment", "apartment"),
    ("House", "house"),
    ("Office", "office"),
    ("Villa", "villa"),
    ("Store", "store"),
    ("Resturant", "resturant")
]

class PropertyAddress(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    longitude = models.IntegerField()
    latitude = models.IntegerField()


class Property(models.Model):
    name = models.CharField(max_length=250)

    status = models.CharField(choices=PROPERTY_STATUS)
    type = models.CharField(choices=PROPERTY_TYPE)

    address = models.ForeignKey(PropertyAddress)
