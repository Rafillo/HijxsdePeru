from django.conf.urls import patterns, include, url
from django.conf import settings
from website.views import PaginaDetailView, BlogDetailView, DocDetailView
from django.views.generic import ListView
from website.models import blog, doc

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^pagina/(?P<pk>\d+)', PaginaDetailView.as_view() ,name='pagina_detail'),
    url(r'^blogs/(?P<pk>\d+)', BlogDetailView.as_view() ,name='blog_detail'),
    url(r'^blogs', ListView.as_view(model=blog) ),
    url(r'^docs/(?P<pk>\d+)', DocDetailView.as_view() ,name='doc_detail'),
    url(r'^docs', ListView.as_view(model=doc) ),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
