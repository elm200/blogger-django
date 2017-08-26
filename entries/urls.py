from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_id>[0-9]+)$', views.show, name='show'),
    url(r'^(?P<entry_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<entry_id>[0-9]+)/update$', views.update, name='update'),
]
