from django.db import models


# Create your models here.
class itemGroup(models.Model):
    group_name = models.CharField(max_length=100, blank=True, default='')
    stock_type = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.group_name


class itemCategories(models.Model):
    group_name = models.ForeignKey(itemGroup, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, blank=True, default='')
    sku_code = models.CharField(max_length=100, blank=True, default='')
    brand = models.CharField(max_length=100, blank=True, default='')
    item_property = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=100, blank=True, default='')
    opening_stock = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.item_name


class stockItem(models.Model):
    sku_code = models.ForeignKey(itemCategories, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank=True, default='')
    model = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=100, blank=True, default='')
    quantity = models.CharField(max_length=100, blank=True, default='')
    net_cost = models.CharField(max_length=100, blank=True, default='')
    vat = models.CharField(max_length=100, blank=True, default='')
    vendor = models.CharField(max_length=100, blank=True, default='')
    non_purchae = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.sku_code
