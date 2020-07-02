from django.shortcuts import render
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
            print("+++++++++++++++++++++++"+request.POST.get('image')+"------------------------------")

            myfile = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            contact.image = request.POST.get('image')

        contact.address = request.POST.get('address')
        contact.city = request.POST.get('city')
        contact.state = request.POST.get('state')
        contact.country = request.POST.get('country')
        contact.phone_number = request.POST.get('phone_number')
        contact.mobile1 = request.POST.get('mobile1')
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
    print(id)
    return render(request, "contact/contact_details.html", context)


def add_contact(request):
    return render(request, "contact/add_contact.html")
