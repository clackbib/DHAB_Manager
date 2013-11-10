from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DHAB_Manager.views.home', name='home'),
    # url(r'^DHAB_Manager/', include('DHAB_Manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include('login.urls')),
    url(r'^projects/', include('project.urls')),
    url(r'^manage/', include("manager.urls")),
    #url(r'^login/$', 'login.views.connect'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
