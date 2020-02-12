from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Activity

def activity(request):
    context = {
        'activities': Activity.objects.all()
    }
    return render(request, 'activity.html', context)


class PostListView(ListView):
    model = Activitie
    template_name = 'activity.html'
    context_object_name = 'activities'