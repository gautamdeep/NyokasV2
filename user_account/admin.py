from django.contrib import admin

from .models import Branch, Tag_for_contacts

# Register your models here.
admin.site.register(Branch)
admin.site.register(Tag_for_contacts)
