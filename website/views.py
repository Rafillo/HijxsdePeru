from models import *
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import TemplateView
from django.views.generic import DetailView

def home(request):
    paginas = pagina.objects.all()[:3]
    blogs = Blog.objects.order_by('-fecha')[:3]
    enlaces = enlace.objects.all()[:5]
    tipos_autor = tipo_autor.objects.all()

    return render_to_response('home.html',{
        'paginas': paginas,
        'blogs': blogs,
        'enlaces': enlaces,
        'tipo_autor': tipo_autor,
    })
