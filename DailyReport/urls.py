from django.urls import path

from . import views

app_name = 'DailyReport'

urlpatterns = [
    path('dailyReport', views.dailyreport, name='app_name'),
    path('dailyReportByFrontDesk', views.dailyReportByFrontDesk, name='dailyReportByFrontDesk'),
    path('daily_work_entry_technical_head/', views.daily_work_entry_technical_head, name="daily_work_entry_technical_head"),
    path('daily_work_entry_manager/', views.daily_work_entry_manager, name="daily_work_entry_manager"),
    path('edit_tech_head/', views.edit_tech_head, name="edit_tech_head"),
    path('updatetechnicalhead/', views.update_technical_head, name="updatetechnicalhead"),

]