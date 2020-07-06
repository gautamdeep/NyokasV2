from django.db import models


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Tag_for_contacts(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name
