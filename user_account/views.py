from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginpage(request):

    if request.user.is_authenticated:
        return redirect('index:index')
    else:

        if request.method == 'POST':
            email = request.POST.get('email')
            password = str(request.POST.get('password'))

            user = authenticate(request, username=email, password=password)
            print(email, password)
            if user is not None:
                login(request, user)
                return redirect('index:index')
            else:
                messages.info(request, 'Email OR password is incorrect')

        context = {}
        return render(request, 'signin.html', context)
