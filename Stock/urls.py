from django.urls import path

from . import views

app_name = 'Stock'

urlpatterns = [
    path('item_group', views.item_group, name='item_group'),
    path('add_item_group', views.add_item_group, name='add_item_group'),

]