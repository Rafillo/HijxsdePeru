from models import *
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import TemplateView
from django.views.generic import DetailView

def home(request):
    paginas = pagina.objects.all()[:5]
    blogs = Blog.objects.order_by('-fecha')[:6]
    enlaces = enlace.objects.all()[:3]
    tipos_autor = tipo_autor.objects.all()

    return render_to_response('home.html',{
        'paginas': paginas,
        'blogs': blogs,
        'enlaces': enlaces,
        'tipo_autor': tipo_autor,
    })

class PaginaDetailView(DetailView):
    queryset = pagina.objects.all()

    def get_object(self):
        object = super(PaginaDetailView, self).get_object()
        return object

class BlogDetailView(DetailView):
    queryset = Blog.objects.all()

    def get_object(self):
        object = super(BlogDetailView, self).get_object()
        return object

class DocDetailView(DetailView):
    queryset = doc.objects.all()

    def get_object(self):
        object = super(DocDetailView, self).get_object()
        return object

class NoticiaDetailView(DetailView):
    queryset = noticia.objects.all()

    def get_object(self):
        object = super(NoticiaDetailView, self).get_object()
        return object
