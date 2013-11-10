from django.conf.urls import patterns, include, url


urlpatterns = patterns('manager.views',

    url(r'^$', 'manage'),

    #url(r'^login/',''),

)