from django.conf.urls import patterns, url


urlpatterns = patterns('manager.views',

                       url(r'^$', 'manage'),
                       url(r'^edit_milestone/(?P<id>\d+)/', 'edit_milestone'),
                       url(r'^delete_milestone/(?P<id>\d+)/', 'delete_milestone'),
                       url(r'^delete_assoc/(?P<id>\d+)/', 'delete_assoc'),
                       url(r'^edit_milestone/(?P<id>\d+)/', 'edit_milestone'),

                       #url(r'^login/',''),

)