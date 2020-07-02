from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [

    path('contact_details/', views.contact_details, name='contact_details'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('add_contact/', views.add_contact, name='add_contact'),

]
