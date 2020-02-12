from django.urls import path
from . import views
from .views import PostListView, CreatingActivityView

urlpatterns = [
    path('', PostListView.as_view(), name='activitie'),
    path('add/', CreatingActivityView.as_view(), name='add-activitie'),
]