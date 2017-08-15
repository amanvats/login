from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.first, name = 'first'),
    url(r'^register/$', views.here.as_view(), name ='here'),
]
