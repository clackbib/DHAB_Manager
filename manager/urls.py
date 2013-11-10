from django.conf.urls import patterns, include, url


urlpatterns = patterns('manager.views',

    url(r'^$', 'manage'),
    url(r'^edit_milestone/(?P<id>\d+)/', 'edit_milestone'),
    url(r'^delete_milestone/(?P<id>\d+)/', 'delete_milestone'),

    #url(r'^login/',''),

)