from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Activitie
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ActivityForm
from django.views import View

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

class CreatingActivityView(LoginRequiredMixin, View ):
    login_url = '/login/'

    def get(self, request):
        form = ActivityForm()
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return render(request, 'user_activities.html', context)

    def post(self, request):
        pass

