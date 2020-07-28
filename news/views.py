from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.

def root(request):
    return HttpResponse('This is the home page') # Not in the LMS
    
def welcome(request):
    return render(request, 'welcome.html')


# Getting news of the day
def news_of_day(request):
    date = dt.date.today()

    # Getting day of the week
    return render(request, 'all-news/today-news.html', {"date": date,})

# Getting days of the week

'''
def convert_dates(dates):
    # Function that gets the weekday number for the date.

    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Returning the actual day of the week
    day = days[day_number]

    return day
'''

# Getting past news

def past_days_news(request, past_date):
    try:
        # Convert data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(news_of_day)
    
    return render(request, 'all-news/past-news.html', {"date": date})