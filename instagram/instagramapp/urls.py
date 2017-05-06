from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.registrar, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
]
