from django.contrib import admin
from .models import itemGroup,itemCategories,stockItem
# Register your models here.
admin.site.register(itemGroup)
admin.site.register(itemCategories)
admin.site.register(stockItem)