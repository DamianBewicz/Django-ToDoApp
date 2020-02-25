from django.urls import path
from . import views
from .views import (
    ActivityListView,
    ActivityUpdateView,
    ActivityCreateView,
    ActivityDetailView,
    ActivityDeleteView
)

urlpatterns = [
    path('', ActivityListView.as_view(), name='activitie'),
    path('add/', ActivityCreateView.as_view(), name='activitie-add'),
    path('<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
]