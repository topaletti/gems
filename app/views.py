from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Company

def index(request):
    return render(request, 'app/index.html')

class DatabaseView(generic.ListView):
    template_name = 'app/database.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.order_by('name')

def challenges(request):
    number_of_days_in_month = 30
    context = {
        'days_of_month': range(1,number_of_days_in_month + 1),
        'last_forecast_day': number_of_days_in_month - 3,
        'length_of_rating_period': number_of_days_in_month - 7,
    }        
    return render(request, 'app/challenges.html', context)
