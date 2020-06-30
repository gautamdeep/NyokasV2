from django.urls import path

from . import views

app_name = 'Product'

urlpatterns = [
    path('vendor', views.vendor, name='vendor'),

]