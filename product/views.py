from django.shortcuts import render, redirect
from .models import Vendor, Purchase_order
from contact.models import Contact


# Create your views here.
def vendor(request):
    context = {
        "vendor": Vendor.objects.all()
    }

    if request.method == 'POST':
        vendor = Vendor()
        vendor.vendor_type = request.POST.get('vendor_type')
        vendor.vendor_name = request.POST.get('vendor_name')
        vendor.address = request.POST.get('address')
        vendor.city = request.POST.get('city')
        vendor.state = request.POST.get('state')
        vendor.country = request.POST.get('country')
        vendor.phone_number = request.POST.get('phone_number')
        vendor.mobile1 = request.POST.get('mobile1')
        vendor.email = request.POST.get('email')
        vendor.pan_no = request.POST.get('pan_no')
        vendor.website = request.POST.get('website')
        vendor.tag = request.POST.get('tag')

        contact = Contact()
        contact.name = request.POST.get('vendor_name')

        contact.address = request.POST.get('address')
        contact.city = request.POST.get('city')
        contact.state = request.POST.get('state')
        contact.country = request.POST.get('country')
        contact.phone_number = request.POST.get('phone_number')
        contact.mobile_number = request.POST.get('mobile1')
        contact.email = request.POST.get('email')
        contact.pan_no = request.POST.get('pan_no')
        contact.website = request.POST.get('website')
        contact.tag = request.POST.get('tag')

        contact.save()


        vendor.save()
        return render(request, 'product/vendor/vendor.html', context)

    else:
        return render(request, 'product/vendor/vendor.html', context)


def add_vendor(request):
    return render(request, 'product/vendor/add_new_vendor.html')


def delete_confirm_vendor(request):
    id = request.GET.get('id')
    context = {
        "vendor": Vendor.objects.get(id=id),
    }

    return render(request, 'product/vendor/delete_vendor.html', context)


def delete_vendor(request):
    id = request.GET.get('id')
    vendor = Vendor.objects.get(id=id)
    if request.method == "POST":
        vendor.delete()
        return redirect('/vendor')

    return vendor(request)


def purchase_order(request):
    context = {
        'purchase_order': Purchase_order.objects.all()

    }

    if request.method == 'POST':
        purchase_order = Purchase_order()
        purchase_order.vendor = Vendor.objects.get(vendor_name=request.POST.get('vendor'))
        purchase_order.vendor_contact1 = request.POST.get('vendor_contact1')
        purchase_order.vendor_contact2 = request.POST.get('vendor_contact2')
        purchase_order.order_date = request.POST.get('order_date')
        purchase_order.order_status = request.POST.get('order_status')
        purchase_order.sub_total = request.POST.get('sub_total')
        purchase_order.tax = request.POST.get('tax')
        purchase_order.tax_amount = request.POST.get('tax_amount')
        purchase_order.total_amount = request.POST.get('total_amount')
        purchase_order.remark = request.POST.get('remark')
        purchase_order.product = request.POST.getlist('product[]')
        purchase_order.qty = request.POST.getlist('qty[]')
        purchase_order.price = request.POST.getlist('price[]')
        purchase_order.total = request.POST.getlist('total[]')
        purchase_order.save()
        return render(request, 'product/purchase_order/purchase_order.html', context)

    else:
        return render(request, 'product/purchase_order/purchase_order.html', context)


def add_purchase_order(request):
    context = {
        "vendor": Vendor.objects.all()
    }
    return render(request, 'product/purchase_order/add_purchase_order.html', context)


def purchase_order_preview(request):
    id = request.GET.get('id')
    purchase_order = Purchase_order.objects.get(id=id)


    context = {
        'purchase_order': purchase_order,
        'a': range(1, len(purchase_order.product) + 1),
        "vendor": Vendor.objects.get(id=purchase_order.vendor_id)
    }

    return render(request, 'product/purchase_order/purchase_order_preview.html', context)
