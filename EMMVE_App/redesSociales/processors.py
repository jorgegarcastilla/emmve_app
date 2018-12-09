from .models import Link

def context_dict(request):
    contexto = {}
    links = Link.objects.all()
    for link in links:
        contexto[link.clave] = link.url
    return contexto