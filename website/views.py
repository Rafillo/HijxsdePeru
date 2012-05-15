from models import *
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import TemplateView
from django.views.generic import DetailView

def home(request):
    paginas = pagina.objects.all()[:5]
    blogs = blog.objects.order_by('-fecha')[:6]
    tipos_autor = tipo_autor.objects.all()
    enlaces = enlace.objects.all()[:3]

    return render_to_response('home.html',{
        'paginas': paginas,
        'blogs': blogs,
        'tipo_autor': tipo_autor,
        'enlaces': enlaces,
    })

class PaginaDetailView(DetailView):
    queryset = pagina.objects.all()

    def get_object(self):
        object = super(PaginaDetailView, self).get_object()
        return object

class BlogDetailView(DetailView):
    queryset = blog.objects.all()

    def get_object(self):
        object = super(BlogDetailView, self).get_object()
        return object

class DocDetailView(DetailView):
    queryset = doc.objects.all()

    def get_object(self):
        object = super(DocDetailView, self).get_object()
        return object
