from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Activitie
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ActivityForm, RawActivityForm
from django.views import View


class ActivityListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Activitie
    template_name = 'activitie.html'
    context_object_name = 'activities'
    ordering = ['to_do_date']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        date_list = []
        for activitie in data['activities']:
            date_list.append(activitie.to_do_date.strftime("%d-%m-%Y"))
        date_activities_dict = {}
        for date in set(date_list):
            date_activities_dict[date] = []
        for key, item in date_activities_dict.items():
            for activitie in data['activities']:
                if key == activitie.to_do_date.strftime("%d-%m-%Y"):
                    date_activities_dict[key].append(activitie)
        converted_list = []
        for key, item in date_activities_dict.items():
            converted_list.append((key, item))
        converted_list.sort()
        print(converted_list)
        data['activities_list'] = converted_list
        return data


class ActivityDetailView(DetailView):
    model = Activitie
    template_name = 'activity_detail.html'


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activitie
    template_name = 'activitie_form.html'
    fields = ['activitie', 'to_do_date', 'is_done']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activitie
    template_name = 'activity_delete.html'
    success_url = '/'

    def test_func(self):
        activitie = self.get_object()
        if self.request.user == activitie.user:
            return True
        return False


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activitie
    template_name = 'activitie_form.html'
    fields = ['activitie', 'to_do_date', 'is_done']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        activitie = self.get_object()
        if self.request.user == activitie.user:
            return True
        return False


class CreateActivityView(LoginRequiredMixin, View):
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