from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Company, Challenge


def index(request):
    return render(request, 'app/index.html')


class DatabaseView(generic.ListView):
    template_name = 'app/database.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.order_by('name')


class ChallengeView(generic.DetailView):
    model = Challenge
    template_name = 'app/challenge.html'
    context_object_name = 'challenge'
