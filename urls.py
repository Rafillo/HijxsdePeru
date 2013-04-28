from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.views.generic import ListView, DetailView
from website.models import Blog, doc, noticia, enlace, galeria, pagina

admin.autodiscover()

urlpatterns = patterns('',
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^$', 'website.views.home', name='home'),
    #url(r'^acerca/', PaginaDetailView.as_view(), name='pagina_detail'),
    url(r'^acerca/', DetailView.as_view(), {"pk": 1}, name="pagina_detail"),
    url(r'^pagina/(?P<pk>\d+)', DetailView.as_view(model=pagina) ,name='pagina_detail'),
    url(r'^blogs/(?P<pk>\d+)', DetailView.as_view(model=Blog) ,name='blog_detail'),
    url(r'^blogs', ListView.as_view(model=Blog) ),
    url(r'^docs/(?P<pk>\d+)', DetailView.as_view(model=doc) ,name='doc_detail'),
    url(r'^docs', ListView.as_view(model=doc) ),
    url(r'^noticias/(?P<pk>\d+)', DetailView.as_view(model=noticia) ,name='noticia_detail'),
    url(r'^noticias', ListView.as_view(model=noticia) ),
    url(r'^enlaces', ListView.as_view(model=enlace) ),
    url(r'^galerias', ListView.as_view(model=galeria) ),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^markitup/', include('markitup.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
