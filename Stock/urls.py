from django.urls import path

from . import views

app_name = 'Stock'

urlpatterns = [
    # itemGroup
    path('item_group/', views.item_group, name='item_group'),
    path('add_item_group/', views.add_item_group, name='add_item_group'),
    path('delete_confirm_item_group/', views.delete_confirm_item_group, name='delete_confirm_item_group'),
    path('delete_item_group/', views.delete_item_group, name='delete_item_group'),

    # item categories
    path('item_categories/', views.item_categories, name="item_categories"),
    path('add_item_categories/', views.add_item_categories, name="add_item_categories"),
    path('delete_confirm_item_category/', views.delete_confirm_item_category, name='delete_confirm_item_category'),
    path('delete_item_category/', views.delete_item_category, name='delete_item_category'),

    # stock  Items
    path('stock_items/', views.stock_items, name="stock_items"),
    path('add_stock_items/', views.add_stock_items, name="add_stock_items"),
    path('delete_confirm_stock_items/', views.delete_confirm_stock_items, name='delete_confirm_stock_items'),
    path('delete_stock_items/', views.delete_stock_items, name='delete_stock_items'),

]
