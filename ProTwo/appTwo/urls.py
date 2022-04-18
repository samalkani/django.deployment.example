from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name="index"),
    url('users/', views.users, name="users"),
    url('help/', views.help, name='help'),
]
