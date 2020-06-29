from django.shortcuts import render, redirect
from .models import itemGroup, itemCategories, stockItem
from django.contrib.auth.models import User


# Create your views here.
def item_group(request):
    context = {
        "itemGroup": itemGroup.objects.all()
    }
    return render(request, 'stock/item_group/item_group.html', context)


def add_item_group(request):
    if request.method == 'POST':
        itemGroups = itemGroup()

        itemGroups.group_name = request.POST.get('group_name')
        itemGroups.stock_type = request.POST.get('stock_type')
        # print(itemGroup)
        itemGroups.save()

        return item_group(request)

    else:
        return item_group(request)


def delete_confirm_item_group(request):
    id = request.GET.get('id')
    context = {
        "itemGroup": itemGroup.objects.get(id=id)
    }
    return render(request, 'stock/item_group/delete_item_group.html', context)


def delete_item_group(request):
    id = request.GET.get('id')
    itemgroup = itemGroup.objects.get(id=id)
    if request.method == "POST":
        itemgroup.delete()
        return redirect('/item_group')

    context = {'itemgroup': itemgroup}
    return item_group(request)


def item_categories(request):
    context = {
        "itemCategories": itemCategories.objects.all()
    }
    if request.method == 'POST':
        Item_categories = itemCategories()
        Item_categories.group_name = itemGroup.objects.get(group_name=request.POST.get('group_name'))
        Item_categories.item_name = request.POST.get('item_name')
        Item_categories.brand = request.POST.get('brand')
        Item_categories.item_property = request.POST.get('item_property')
        Item_categories.unit = request.POST.get('unit')
        Item_categories.sku_code = request.POST.get('sku_code')
        Item_categories.opening_stock = request.POST.get('opening_stock')
        # print(itemGroup)
        Item_categories.save()

        return render(request, 'stock/item_categories/item_categories.html', context)
    else:
        return render(request, 'stock/item_categories/item_categories.html', context)


def add_item_categories(request):
    context = {
        "itemGroup": itemGroup.objects.all()
    }
    '''
    if request.method == 'POST':
        Item_categories = itemCategories()
        Item_categories.group_name = itemGroup.objects.get(group_name=request.POST.get('group_name'))
        Item_categories.item_name = request.POST.get('item_name')
        Item_categories.brand = request.POST.get('brand')
        Item_categories.item_property = request.POST.get('item_property')
        Item_categories.unit = request.POST.get('unit')
        Item_categories.sku_code = request.POST.get('sku_code')
        Item_categories.opening_stock = request.POST.get('opening_stock')
        # print(itemGroup)
        Item_categories.save()
        return render(request, 'stock/item_categories/add_item_categories.html', context)


    else:'''
    return render(request, 'stock/item_categories/add_item_categories.html', context)


def delete_confirm_item_category(request):
    id = request.GET.get('id')
    context = {
        "itemCategories": itemCategories.objects.get(id=id),
        'id': id
    }
    return render(request, 'stock/item_categories/delete_item_categories.html', context)


def delete_item_category(request):
    id = request.GET.get('id')
    ItemCategories = itemCategories.objects.get(id=id)
    if request.method == "POST":
        ItemCategories.delete()
        return redirect('/item_categories')

    return item_categories(request)


def stock_items(request):
    context = {
        "stockItem": stockItem.objects.all()
    }
    if request.method == 'POST':
        StockItem = stockItem()
        StockItem.sku_code = itemCategories.objects.get(sku_code=request.POST.get('sku_code'))
        StockItem.brand = request.POST.get('brand')
        StockItem.model = request.POST.get('model')
        StockItem.quantity = request.POST.get('quantity')
        StockItem.unit = request.POST.get('unit')
        StockItem.net_cost = request.POST.get('net_cost')
        StockItem.vat = request.POST.get('vat')
        StockItem.vendor = request.POST.get('vendor')
        StockItem.non_purchae = request.POST.get('non_purchae')
        # print(itemGroup)
        StockItem.save()
        return render(request, 'stock/stock_item/stock_item.html', context)

    else:
        return render(request, 'stock/stock_item/stock_item.html', context)

    return render(request, 'stock/stock_item/stock_item.html', context)


def add_stock_items(request):
    context = {
          "itemCategories": itemCategories.objects.all()
    }

    return render(request, 'stock/stock_item/add_stock_item.html', context)


def delete_confirm_stock_items(request):
    id = request.GET.get('id')
    context = {
        "stockItem": stockItem.objects.get(id=id),
    }
    return render(request, 'stock/stock_item/delete_stock_item.html', context)


def delete_stock_items(request):
    id = request.GET.get('id')
    StockItem = stockItem.objects.get(id=id)
    if request.method == "POST":
        StockItem.delete()
        return redirect('/stock_items')

    return stock_items(request)
