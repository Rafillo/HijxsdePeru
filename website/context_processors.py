from models import blog, enlace

def sidebar(request):
    blogs = blog.objects.order_by('-fecha')[:6]
    enlaces = enlace.objects.all()[:3]
    return {
        'blogs': blogs,
        'enlaces': enlaces,
    }

