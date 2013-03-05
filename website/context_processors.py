from models import Blog, enlace

def sidebar(request):
    blogs = Blog.objects.order_by('-fecha')[:6]
    enlaces = enlace.objects.all()[:3]
    return {
        'blogs': blogs,
        'enlaces': enlaces,
    }

