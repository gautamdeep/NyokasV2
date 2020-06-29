from django.shortcuts import render
from .models import itemGroup, itemCategories, stockItem
from django.contrib.auth.models import User


# Create your views here.
def item_group(request):
    return render(request, 'stock/item_group/itemgroup.html')


def add_item_group(request):
    if request.method == 'POST':
        itemGroups = itemGroup()

        itemGroups.date = request.POST.get('date')
        itemGroups.problem = request.POST.get('problem')
        itemGroups.save()

        return render(request, 'stock/item_group/add_item_group.html')

    else:
        return render(request, 'stock/item_group/add_item_group.html')

