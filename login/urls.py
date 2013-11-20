from django.conf.urls import patterns, url


urlpatterns = patterns('login.views',

                       url(r'^$', 'register'),
                       url(r'^login/', 'connect'),
                       url(r'^logout/', 'disconnect'),

)