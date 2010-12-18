from django.conf.urls.defaults import *

urlpatterns = patterns('divelog.views',
    (r'^$', 'index'),
    (r'^(?P<dive_id>\d+)/$', 'detail'),
    )
