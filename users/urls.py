from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import signup, login


urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),

]