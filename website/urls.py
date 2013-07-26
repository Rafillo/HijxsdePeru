from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView

from website.models import Blog, Doc, Noticia, Enlace, Galeria, Pagina
from website.views import BlogDetailView, TagDetailView, Carta
from website import views

urlpatterns = patterns('',
    url(r'^pagina/(?P<pk>\d+)', DetailView.as_view(model=Pagina), name='pagina_detail'),
    url(r'^blogs/(?P<pk>\d+)/(?P<slug>[-\w\d]+)', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<pk>\d+)', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs', ListView.as_view(model=Blog) ),
    url(r'^docs/(?P<pk>\d+)/(?P<slug>[-\w\d]+)', DetailView.as_view(model=Doc), name='doc_detail'),
    url(r'^docs/(?P<pk>\d+)', DetailView.as_view(model=Doc), name='doc_detail'),
    url(r'^docs', ListView.as_view(model=Doc) ),
    url(r'^noticias/(?P<pk>\d+)/(?P<slug>[-\w\d]+)', DetailView.as_view(model=Noticia), name='noticia_detail'),
    url(r'^noticias/(?P<pk>\d+)', DetailView.as_view(model=Noticia), name='noticia_detail'),
    url(r'^noticias', ListView.as_view(model=Noticia) ),
    url(r'^enlaces', ListView.as_view(model=Enlace) ),
    url(r'^galerias', ListView.as_view(model=Galeria) ),
    url(r'^carta', Carta, name='carta' ),
    url(r'^enviada', TemplateView.as_view(template_name='website/enviada.html')),
)
