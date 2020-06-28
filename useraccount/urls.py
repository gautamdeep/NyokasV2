from django.urls import path

from . import views

app_name = 'useraccount'

urlpatterns = [
    path('login/', views.loginpage, name='login'),

]
