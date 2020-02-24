from django.shortcuts import render
from django.views.generic import ListView
from .models import Activitie
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ActivityForm, RawActivityForm
from django.views import View



class PostListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Activitie
    template_name = 'activitie.html'
    context_object_name = 'activities'

    def get_queryset(self):
        query_set=super().get_queryset()
        return query_set.filter(user=self.request.user)

class CreatingActivityView(LoginRequiredMixin, View):
    login_url = '/login/'
    form = RawActivityForm()

    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, 'user_activities.html', context)

    def post(self, request):
        if form.is_valid():
            form.save()
        context = {
            'form': self.form
        }
        return render(request, 'user_activities.html', context)