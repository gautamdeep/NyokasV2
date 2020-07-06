from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [

    path('contact_details/', views.contact_details, name='contact_details'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('delete_confirm/', views.delete_confirm, name='delete_confirm'),
    path('delete_contact/', views.delete_contact, name='delete_contact'),
    path('edit_contact/', views.edit_contact, name='edit_contact'),
    path('update_contact/', views.update_contact, name='update_contact'),

]
