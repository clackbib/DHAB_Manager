from django.conf.urls import patterns, url


urlpatterns = patterns('reports.views',

                       url(r'^$', 'reports'),


                       #url(r'^login/',''),

)