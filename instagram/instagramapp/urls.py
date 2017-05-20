from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.registrar, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^crear_usuario/$', views.crear_usuario, name='crear_usuario'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
]
