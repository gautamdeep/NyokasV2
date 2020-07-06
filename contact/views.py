from django.shortcuts import render, redirect
from .models import Contact
from django.core.files.storage import FileSystemStorage


# Create your views here.
def contact_list(request):
    context = {
        'contact': Contact.objects.all()
    }

    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.gender = request.POST.get('gender')
        if request.POST.get('image') == "":
            pass
        else:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            contact.image = myfile

        contact.address = request.POST.get('address')
        contact.city = request.POST.get('city')
        contact.state = request.POST.get('state')
        contact.country = request.POST.get('country')
        contact.phone_number = request.POST.get('phone_number')
        contact.mobile_number = request.POST.get('mobile_number')
        contact.email = request.POST.get('email')
        contact.pan_no = request.POST.get('pan_no')
        contact.website = request.POST.get('website')
        contact.tag = request.POST.get('tag')
        contact.job_position = request.POST.get('job_position')

        contact.save()
        return render(request, "contact/contact_list.html", context)
    else:
        return render(request, "contact/contact_list.html", context)


def contact_details(request):
    id = request.GET.get('id')
    context = {
        'contact': Contact.objects.get(id=id)
    }
    return render(request, "contact/contact_details.html", context)


def add_contact(request):
    return render(request, "contact/add_contact.html")


def delete_confirm(request):
    id = request.GET.get('id')
    context = {
        "contact": Contact.objects.get(id=id),
    }
    return render(request, "contact/delete_confirm.html", context)


def delete_contact(request):
    id = request.GET.get('id')
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        return redirect('/contact_list')

    return contact_list(request)


def edit_contact(request):
    id = request.GET.get('id')

    context = {
        'contact': Contact.objects.get(id=id),
        'id': id
    }

    return render(request, "contact/edit_contact.html", context)


def update_contact(request):
    id = request.GET.get('id')
    print(id)

    if request.method == 'POST':
        contact = Contact.objects.get(id=id)
        contact.name = request.POST.get('name')
        contact.gender = request.POST.get('gender')
        if request.POST.get('image') == "":
            pass
        else:
            # print("+++++++++++++++++++++++"+request.POST.get('image')+"------------------------------")
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            contact.image = myfile

        contact.address = request.POST.get('address')
        contact.city = request.POST.get('city')
        contact.state = request.POST.get('state')
        contact.country = request.POST.get('country')
        contact.phone_number = request.POST.get('phone_number')
        contact.mobile_number = request.POST.get('mobile_number')
        contact.email = request.POST.get('email')
        contact.pan_no = request.POST.get('pan_no')
        contact.website = request.POST.get('website')
        contact.tag = request.POST.get('tag')
        contact.job_position = request.POST.get('job_position')

        contact.save()

        return redirect("/contact_list/")
