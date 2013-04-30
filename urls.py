from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.views.generic import ListView, DetailView
from website.models import Blog, Doc, Noticia, Enlace, Galeria, Pagina
from website.views import BlogDetailView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^markitup/', include('markitup.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^contacto/', include("contact_form.urls", namespace="contact_form")),
    url(r'^$', 'website.views.home', name='home'),
    url(r'^acerca/', DetailView.as_view(model=Pagina), {"pk": 1}, name="pagina_detail"),

    #mover esto a website? url(r'^/', include('polls.urls')),
    url(r'^pagina/(?P<pk>\d+)', DetailView.as_view(model=Pagina) ,name='pagina_detail'),
    url(r'^blogs/(?P<pk>\d+)', BlogDetailView.as_view(model=Blog) ,name='blog_detail'),
    url(r'^blogs', ListView.as_view(model=Blog) ),
    url(r'^docs/(?P<pk>\d+)', DetailView.as_view(model=Doc) ,name='doc_detail'),
    url(r'^docs', ListView.as_view(model=Doc) ),
    url(r'^noticias/(?P<pk>\d+)', DetailView.as_view(model=Noticia) ,name='noticia_detail'),
    url(r'^noticias', ListView.as_view(model=Noticia) ),
    url(r'^enlaces', ListView.as_view(model=Enlace) ),
    url(r'^galerias', ListView.as_view(model=Galeria) ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
