from django.conf.urls import url, include
from . import views


app_name = 'classifier'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='all-images'),
    url(r'^upload/$', views.Upload.as_view(), name='upload'),
    url(r'^image/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='get-image'),
]
