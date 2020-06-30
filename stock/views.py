from django.shortcuts import render, redirect
from .models import ItemGroup, ItemCategories, StockItem
from django.contrib.auth.models import User


# Create your views here.
def item_group(request):
    context = {
        "itemGroup": ItemGroup.objects.all()
    }
    return render(request, 'stock/item_group/item_group.html', context)


def add_item_group(request):
    if request.method == 'POST':
        itemGroups = ItemGroup()

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
        "itemGroup": ItemGroup.objects.get(id=id)
    }
    return render(request, 'stock/item_group/delete_item_group.html', context)


def delete_item_group(request):
    id = request.GET.get('id')
    itemgroup = ItemGroup.objects.get(id=id)
    if request.method == "POST":
        itemgroup.delete()
        return redirect('/item_group')

    context = {'itemgroup': itemgroup}
    return item_group(request)


def item_categories(request):
    context = {
        "itemCategories": ItemCategories.objects.all()
    }
    if request.method == 'POST':
        Item_categories = ItemCategories()
        Item_categories.group_name = ItemGroup.objects.get(group_name=request.POST.get('group_name'))
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
        "itemGroup": ItemGroup.objects.all()
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
        "itemCategories": ItemCategories.objects.get(id=id),
        'id': id
    }
    return render(request, 'stock/item_categories/delete_item_categories.html', context)


def delete_item_category(request):
    id = request.GET.get('id')
    itemCategories = ItemCategories.objects.get(id=id)
    if request.method == "POST":
        itemCategories.delete()
        return redirect('/item_categories')

    return item_categories(request)


def stock_items(request):
    context = {
        "stockItem": StockItem.objects.all()
    }
    if request.method == 'POST':
        Stock_Item = StockItem()
        Stock_Item.sku_code = ItemCategories.objects.get(sku_code=request.POST.get('sku_code'))
        Stock_Item.brand = request.POST.get('brand')
        Stock_Item.model = request.POST.get('model')
        Stock_Item.quantity = request.POST.get('quantity')
        Stock_Item.unit = request.POST.get('unit')
        Stock_Item.net_cost = request.POST.get('net_cost')
        Stock_Item.vat = request.POST.get('vat')
        Stock_Item.vendor = request.POST.get('vendor')
        Stock_Item.non_purchae = request.POST.get('non_purchae')

        Stock_Item.save()
        return render(request, 'stock/stock_item/stock_item.html', context)

    else:
        return render(request, 'stock/stock_item/stock_item.html', context)


def add_stock_items(request):
    context = {
        "itemCategories": ItemCategories.objects.all()
    }

    return render(request, 'stock/stock_item/add_stock_item.html', context)


def delete_confirm_stock_items(request):
    id = request.GET.get('id')
    context = {
        "stockItem": StockItem.objects.get(id=id),
    }
    return render(request, 'stock/stock_item/delete_stock_item.html', context)


def delete_stock_items(request):
    id = request.GET.get('id')
    Stock_Item = StockItem.objects.get(id=id)
    if request.method == "POST":
        Stock_Item.delete()
        return redirect('/stock_items')

    return stock_items(request)
