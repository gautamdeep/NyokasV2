from django.db import models

GENDER = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, blank=True, default='')
    profile_image = models.ImageField(default='default-avatar.png', null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=25, default='')

    phone_number = models.CharField(max_length=12, blank=True, default='')
    mobile_number = models.CharField(max_length=12, blank=True, default='')
    email = models.CharField(max_length=500, blank=True, default='')

    job_position = models.CharField(max_length=12, blank=True, default='')

    # address
    address = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    
    pan_no = models.CharField(max_length=100, blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')
    tag = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name
