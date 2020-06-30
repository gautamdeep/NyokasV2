from django.urls import path

from . import views

app_name = 'Product'

urlpatterns = [
    path('vendor', views.vendor, name='vendor'),
    path('add_vendor/', views.add_vendor, name='add_vendor'),
    path('delete_confirm_vendor/', views.delete_confirm_vendor, name='delete_confirm_vendor'),
    path('delete_vendor/', views.delete_vendor, name='delete_vendor'),

]