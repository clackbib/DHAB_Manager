from django.conf.urls import patterns, include, url


urlpatterns = patterns('reports.views',

    url(r'^$', 'reports'),


    #url(r'^login/',''),

)