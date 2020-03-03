from django.shortcuts import render
from datetime import datetime
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ActivityForm, RawActivityForm
from django.views import View


class ActivityListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Activity
    template_name = 'activity.html'
    context_object_name = 'activities'
    ordering = ['-to_do_date']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouped_activities = []
        current_date = None
        current_activities = []
        for activity in context['activities']:
            if activity.to_do_date.date() != current_date:
                if current_date is not None:
                    grouped_activities.append((current_date, current_activities))
                    current_activities = []
                current_date = activity.to_do_date.date()
            current_activities.append(activity)
        grouped_activities.append((current_date, current_activities))
        context['grouped_activities'] = grouped_activities
        return context


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    template_name = 'activity_form.html'
    fields = ['activity', 'to_do_date', 'is_done']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def dupa(request):
    import pdb;pdb.set_trace()
    print(request)


class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    template_name = 'activity_delete.html'
    success_url = '/'

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.user:
            return True
        return False


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    template_name = 'activity_form.html'
    fields = ['activity', 'to_do_date', 'is_done']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.user:
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