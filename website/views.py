from django.shortcuts import render_to_response, render
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from taggit.models import TaggedItem, Tag

from models import Blog, Foto, Noticia, Enlace, Perfil, Pagina
from settings import CARTA_TO, CARTA_FROM
from forms import CartaForm

def home(request):
    noticias = Noticia.objects.all()[:3]
    blogs = Blog.objects.order_by('-fecha')[:3]

    return render(request, 'home.html',{
        'noticias': noticias,
        'blogs': blogs,
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
        noticias = Noticia.objects.filter(tags__name__in=[context['tag'].name])
        context['noticias'] = noticias
        return context

def Carta(request):
    carta = Pagina.objects.get(pk=17) # Cartas
    if request.method == 'POST':
        form = CartaForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "Asunto: " + form.cleaned_data['asunto']
            message = "Mensaje: " + form.cleaned_data['mensaje']
            sender = "Remitente: " + form.cleaned_data['nombre_remitente'] + " " + form.cleaned_data['correo_remitente']
            cc = form.cleaned_data['cc']
            if cc:
                recipients.append(sender_email)
            body = sender + "\n" + subject + "\n" + message + "\n" + sender + "\n"
            email = EmailMessage('CARTA Hijxs', body, CARTA_FROM, CARTA_TO)
            if request.FILES:
                email.attach(request.FILES['archivo'].name, request.FILES['archivo'].read())
            email.send()
            return HttpResponseRedirect('/enviada')
    else:
        form = CartaForm()

    return render(request, 'website/carta.html', {
        'form': form,
        'carta': carta,
    })
