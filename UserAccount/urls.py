from django.urls import path

from . import views

app_name = 'UserAccount'

urlpatterns = [
    path('login/', views.loginpage, name='login'),

]
