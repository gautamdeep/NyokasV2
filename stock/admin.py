from django.contrib import admin
from .models import ItemGroup,ItemCategories,StockItem
# Register your models here.
admin.site.register(ItemGroup)
admin.site.register(ItemCategories)
admin.site.register(StockItem)