from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Sathvik"
    month = month.capitalize()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)
    now = datetime.now()
    cal = HTMLCalendar().formatmonth(year, month_num)

    return render(request, 'home.html',
                  {'name': name, "year": year, "month": month, 'month_num': month_num,
                   'cal': cal, "now": now})
