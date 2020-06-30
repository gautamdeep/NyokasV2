from django.db import models
from django.contrib.postgres.fields import ArrayField


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


class Purchase_order(models.Model):
    product = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True, default=''),
            size=10
        ),
        size=10
    )
    qty = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True, default=''),
            size=10
        ),
        size=10
    )
    price = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True, default=''),
            size=10
        ),
        size=10
    )
    total = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True, default=''),
            size=10
        ),
        size=10
    )

    vendor = models.CharField(max_length=100, blank=True, default='')
    vendor_contact1 = models.CharField(max_length=100, blank=True, default='')
    vendor_contact2 = models.CharField(max_length=100, blank=True, default='')
    order_date = models.CharField(max_length=100, blank=True, default='')
    order_status = models.CharField(max_length=100, blank=True, default='')
    sub_total = models.CharField(max_length=100, blank=True, default='')
    tax = models.CharField(max_length=100, blank=True, default='')

    tax_amount = models.CharField(max_length=100, blank=True, default='')
    total_amount = models.CharField(max_length=100, blank=True, default='')
    remark = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.order_status
