from django.conf.urls import url
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^registration/$', views.Registration.as_view(), name='registration'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
]
