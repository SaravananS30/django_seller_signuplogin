from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class gogreenerapp(models.Model):
    CITY_CHOICES = (
        ('', '--Select an option--'),
        ('sydney', 'Sydney'),
        ('brisbane', 'Brisbane'),
        ('melbourne', 'Melbourne'),
        ('canberra', 'Canberra')
    )
    DELIVERY_RANGE = (
        ('', '--Select an option--'),
        (4, 'Upto 4km'),
        (5, 'Upto 5km'),
        (6, 'Upto 6km'),
        (7, 'Upto 7km')
    )
    ID_CHOICES = (
        ('', '--Select an option--'),
        (1, 'GOGROCER101'),
        (2, 'GOGROCER102'),
        (3, 'GOGROCER103'),
        (4, 'GOGROCER104')
    )
    ADMIN_SHARE = (
        ('', '--Select your option--'),
        ('Membership', 'You will be charged a monthly or yearly fee'),
        ('Commission', '10% commission per order')
    )
    LANGUAGE_CHOICES = (
        ('', '--select an option--'),
        ('English', 'English'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
        ('Malayalam', 'Malayalam'),
        ('Telugu', 'Telugu')
    )

    seller_name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100, unique=True)
    store_number = models.BigIntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    admin_share = models.CharField(max_length=100, choices=ADMIN_SHARE)
    password = models.CharField(max_length=100)
    select_city = models.CharField(max_length=100, choices=CITY_CHOICES)
    delivery_range = models.IntegerField(null=True, choices=DELIVERY_RANGE)
    store_address = models.CharField(max_length=100)
    select_id = models.IntegerField(null=True, choices=ID_CHOICES)
    language = models.CharField(max_length=20,null=True,blank=True, choices=LANGUAGE_CHOICES)
