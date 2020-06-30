from django.db import models


# Create your models here.
class Vendor(models.Model):
    vendor_type = models.CharField(max_length=100, blank=True, default='')
    vendor_name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    phone_number = models.CharField(max_length=100, blank=True, default='')
    mobile1 = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')

    pan_no = models.CharField(max_length=100, blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')
    tag = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.vendor_name
