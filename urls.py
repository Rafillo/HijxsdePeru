from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.views.generic import ListView, DetailView
from website.models import Blog, Doc, Noticia, Enlace, Galeria, Pagina
from website.views import BlogDetailView, TagDetailView
from taggit.models import TaggedItem

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^markitup/', include('markitup.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^contacto/', include("contact_form.urls", namespace="contact_form")),
    url(r'^$', 'website.views.home', name='home'),
    url(r'^acerca/', DetailView.as_view(model=Pagina), {"pk": 1}, name="pagina_detail"),
    #url(r'^etiqueta/', ListView.as_view(model=TaggedItem), name="tag_list"),
    url(r'^etiqueta/(?P<slug>[-\w\d]+)', TagDetailView.as_view(), name="tag_detail"),

    url(r'', include('website.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
