from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('vendor', views.vendor, name='vendor'),
    path('add_vendor/', views.add_vendor, name='add_vendor'),
    path('delete_confirm_vendor/', views.delete_confirm_vendor, name='delete_confirm_vendor'),
    path('delete_vendor/', views.delete_vendor, name='delete_vendor'),

    path('purchase_order/', views.purchase_order, name='purchase_order'),
    path('add_purchase_order/', views.add_purchase_order, name='add_purchase_order'),
    path('purchase_order_preview/', views.purchase_order_preview, name='purchase_order_preview'),

]