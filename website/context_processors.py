from models import Blog, Enlace

def sidebar(request):
    side_docs = Blog.objects.order_by('-fecha')[:6]
    side_enlaces = Enlace.objects.all()[:3]
    return {
        'side_docs': side_docs,
        'side_enlaces': side_enlaces,
    }

