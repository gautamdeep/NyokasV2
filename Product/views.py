from django.shortcuts import render, redirect
from .models import Vendor


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
    product = request.POST.getlist('product[]')
    print(product)
    return render(request, 'product/purchase_order/purchase_order.html')


def purchase_order_preview(request):
    return render(request, 'product/purchase_order/purchase_order_preview.html')
