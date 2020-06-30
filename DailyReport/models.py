from django.db import models
from django.contrib.auth.models import User
from Stock.models import itemCategories

Lservice = (('Installation', 'Installation'), ('Service/Repair', 'Service/Repair'), ('', 'default'))


# Create your models here.
class DailyWorkReport(models.Model):
    token = models.CharField(max_length=100, blank=True, default='')

    date = models.DateField(null=True, blank=True)
    site_name = models.CharField(max_length=100, blank=True, default='')
    representative = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    landmark = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    contact = models.CharField(max_length=100, blank=True, default='')
    contact2 = models.CharField(max_length=100, blank=True, default='')
    service = models.CharField(choices=Lservice, max_length=25, default='', blank=True)
    problem = models.CharField(max_length=100, blank=True, default='')
    assign_to = models.CharField(max_length=100, blank=True, default='')
    service_report = models.CharField(max_length=100, blank=True, default='')
    bill_no = models.CharField(max_length=100, blank=True, default='')
    bill_amount = models.CharField(max_length=100, blank=True, default='')
    bill_submit = models.CharField(max_length=100, blank=True, default='')
    amount_received = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.site_name
