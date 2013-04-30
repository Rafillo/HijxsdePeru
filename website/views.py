from models import Blog, Foto, Pagina
from django.shortcuts import render_to_response
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

class BlogDetailView(DetailView):

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        fotos = Foto.objects.filter(galeria=context['blog'].galeria_id)
        context['fotos'] = fotos
        return context
