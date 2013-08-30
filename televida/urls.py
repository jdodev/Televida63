from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'televida63.views.inicio', name='inicio'),
    # url(r'^televida/', include('televida.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'Noticia/(?P<IdNoticia>\d+)/$', 'televida63.views.VerNoticia', name='VerNoticia'),
    url(r'Noticia/Archivo/$', 'televida63.views.VerNoticiasTodos', name='VerNoticiasTodos'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT},
        ),
)
