from django.urls import path
from . import views

urlpatterns = [
    path('activity/', views.activity, name='activity'),
]