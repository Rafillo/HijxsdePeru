from django.shortcuts import render_to_response
from django.views.generic import DetailView

from taggit.models import TaggedItem, Tag
from models import Blog, Foto, Noticia, Enlace

def home(request):
    noticias = Noticia.objects.all()[:3]
    blogs = Blog.objects.order_by('-fecha')[:3]
    enlaces = Enlace.objects.all()[:2]

    return render_to_response('home.html',{
        'noticias': noticias,
        'blogs': blogs,
        'enlaces': enlaces,
    })

class BlogDetailView(DetailView):

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        fotos = Foto.objects.filter(galeria=context['blog'].galeria_id)
        context['fotos'] = fotos
        return context

class TagDetailView(DetailView):

    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        #blogs = Blog.objects.filter(tags__name__in=['Arte'])
        blogs = Blog.objects.filter(tags__name__in=[context['tag'].name])
        context['blogs'] = blogs
        return context
