from models import Doc, Enlace

def sidebar(request):
    side_docs = Doc.objects.order_by('-fecha')[:6]
    side_enlaces = Enlace.objects.all()[:3]
    return {
        'side_docs': side_docs,
        'side_enlaces': side_enlaces,
    }

