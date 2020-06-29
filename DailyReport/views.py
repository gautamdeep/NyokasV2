from django.shortcuts import render
from .models import DailyWorkReport
from django.contrib.auth.models import User


# Create your views here.
def dailyreport(request):
    context = {
        "dailyreport": DailyWorkReport.objects.all()
    }
    return render(request, "daily_report/daily_work_report.html", context)


def dailyReportByFrontDesk(request):
    import time
    from datetime import datetime, timezone
    import pytz
    tz = pytz.timezone('Asia/Kathmandu')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))

    if request.method == 'POST':
        dailyWorkReport = DailyWorkReport()
        dailyWorkReport.token = millis

        dailyWorkReport.date = request.POST.get('date')

        dailyWorkReport.site_name = request.POST.get('site_name')
        dailyWorkReport.representative = request.POST.get('representative')
        dailyWorkReport.address = request.POST.get('address')
        dailyWorkReport.landmark = request.POST.get('landmark')
        dailyWorkReport.city = request.POST.get('city')
        dailyWorkReport.contact = request.POST.get('contact')
        dailyWorkReport.contact2 = request.POST.get('contact2')
        dailyWorkReport.service = request.POST.get('service')
        dailyWorkReport.problem = request.POST.get('problem')
        dailyWorkReport.save()

        return render(request, 'daily_report/dailyReportByFrontDesk.html')

    else:
        return render(request, 'daily_report/dailyReportByFrontDesk.html')



def daily_work_entry_technical_head(request):
    context = {
        "dailyreport": DailyWorkReport.objects.all()
    }
    return render(request, "daily_report/daily_work_entry_technical_head.html", context)


def edit_tech_head(request):
    id = request.GET.get('id')
    return render(request, 'daily_report/updatedailyreportbytechnicalhead.html', {'id': id})


def update_technical_head(request):
    i = request.POST.get('id')
    print(i)
    if request.method == 'POST':
        tech = DailyWorkReport.objects.get(token=i)
        print(request.POST.get('service_report'))
        tech.assign_to = request.POST.get('assign_to')
        tech.service_report = request.POST.get('service_report')
        tech.save()
    return daily_work_entry_technical_head(request)


def daily_work_entry_manager(request):
    context = {
        "dailyreport": DailyWorkReport.objects.all()
    }
    return render(request, "daily_report/daily_work_entry_manager.html", context)


def manager_edit_daily_report(request):
    id = request.GET.get('id')
    return render(request, 'daily_report/update_daily_report_by_manager.html', {'id':  id})


def manager_update_daily_report(request):
    i = request.POST.get('id')
    print(i)
    if request.method == 'POST':
        tech = DailyWorkReport.objects.get(token=i)
        tech.bill_no = request.POST.get('bill_no')
        tech.bill_amount = request.POST.get('bill_amount')
        tech.bill_submit = request.POST.get('bill_submit')
        tech.amount_received = request.POST.get('amount_received')
        tech.save()

    return daily_work_entry_manager(request)
