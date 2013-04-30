from models import Blog, Enlace

def sidebar(request):
    blogs = Blog.objects.order_by('-fecha')[:6]
    enlaces = Enlace.objects.all()[:3]
    return {
        'blogs': blogs,
        'enlaces': enlaces,
    }

