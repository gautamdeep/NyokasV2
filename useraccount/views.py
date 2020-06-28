from django.shortcuts import render,redirect

# Create your views here.
def loginpage(request):
    '''
    if request.user.is_authenticated:
        return redirect('home:index')
    else:

        if request.method == 'POST':
            email = request.POST.get('email')
            password = str(request.POST.get('password'))

            user = authenticate(request, username=email, password=password)
            print(email, password)
            if user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                messages.info(request, 'Email OR password is incorrect')

'''
    context = {}
    return render(request, 'useraccount/login.html', context)
