from django.conf.urls import patterns, include, url


urlpatterns = patterns('project.views',

    url(r'^$', 'projects'),
    url(r'^add/', 'add_project'),
    url(r'^update/', 'update_project'),
    url(r'^requirements/', 'requirements'),
    url(r'^edit_requirement/(?P<id>\d+)/', 'edit_requirement'),
    url(r'^delete_requirement/(?P<id>\d+)/', 'delete_requirement')
    #url(r'^login/',''),

)
