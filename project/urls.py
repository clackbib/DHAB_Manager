from django.conf.urls import patterns, include, url


urlpatterns = patterns('project.views',

    url(r'^$', 'projects'),
    url(r'^add/', 'add_project'),
    url(r'^update/', 'update_project'),
    url(r'^requirements/', 'requirements'),
    #url(r'^login/',''),

)
