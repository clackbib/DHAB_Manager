from django.conf.urls import patterns, include, url


urlpatterns = patterns('project.views',

    url(r'^$', 'project'),
    #url(r'^login/',''),

)
