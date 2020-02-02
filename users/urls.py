from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SignupView, login


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),

]