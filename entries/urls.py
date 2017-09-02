from django.conf.urls import url

from entries.views import entry

urlpatterns = [
    url(r'^$', entry.index, name='index'),
    url(r'^(?P<entry_id>[0-9]+)$', entry.show, name='show'),
    url(r'^new$', entry.new, name='new'),
    url(r'^create$', entry.create, name='create'),
    url(r'^(?P<entry_id>[0-9]+)/edit$', entry.edit, name='edit'),
    url(r'^(?P<entry_id>[0-9]+)/update$', entry.update, name='update'),
    url(r'^(?P<entry_id>[0-9]+)/destroy$', entry.destroy, name='destroy'),
]
