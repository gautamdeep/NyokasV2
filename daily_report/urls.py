from django.urls import path

from . import views

app_name = 'daily_report'

urlpatterns = [
    path('daily_report', views.dailyreport, name='app_name'),
    path('dailyReportByFrontDesk', views.dailyReportByFrontDesk, name='dailyReportByFrontDesk'),
    path('daily_work_entry_technical_head/', views.daily_work_entry_technical_head, name="daily_work_entry_technical_head"),
    path('edit_tech_head/', views.edit_tech_head, name="edit_tech_head"),
    path('updatetechnicalhead/', views.update_technical_head, name="updatetechnicalhead"),


    path('daily_work_entry_manager/', views.daily_work_entry_manager, name="daily_work_entry_manager"),
    path('manager_edit_daily_report/', views.manager_edit_daily_report,
         name="manager_edit_daily_report"),
    path('manager_update_daily_report/', views.manager_update_daily_report, name="manager_update_daily_report"),

]