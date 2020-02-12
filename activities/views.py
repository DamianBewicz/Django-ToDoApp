from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Activitie
from django.contrib.auth.mixins import LoginRequiredMixin

def activitie(request):
    context = {
        'activities': Activitie.objects.all()
    }
    return render(request, 'activitie.html', context)

class PostListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Activitie
    template_name = 'activitie.html'
    context_object_name = 'activities'