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
    url(r'^Noticia/(?P<IdNoticia>\d+)/$', 'televida63.views.VerNoticia', name='VerNoticia'),
    url(r'^Blogs/(?P<IdBlogP>\d+)/$', 'televida63.views.VerEntradasBlog', name='VerEntradasBlog'),
    url(r'^Noticia/Archivo/$', 'televida63.views.VerNoticiasTodos', name='VerNoticiasTodos'),
    url(r'^Blogs/$', 'televida63.views.ListaBlogs', name='ListaBlogs'),
    url(r'^Contactanos/$', 'televida63.views.contacto', name='contacto'),
    url(r'^poll/', include('poll.urls')),
    url(r'^Buscar/$', 'televida63.views.BuscarNoticia', name='BuscarNoticia'),
    url(r'^Programacion$',)
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT},
        ),
)
