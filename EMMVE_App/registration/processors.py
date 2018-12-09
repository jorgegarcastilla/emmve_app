from .models import Persona,Gestor,Docente

def context_dict(request):
    if request.user.is_authenticated:
        persona = Persona.objects.get(user_id=request.user.id)
        perfilUsuario = persona.tipoPerfil
        pk_persona = persona.id
    else:
        perfilUsuario='NOT'
        pk_persona = None
    print(perfilUsuario)
    print(pk_persona)
    contexto = {'perfilUsuario':perfilUsuario,'pk_persona':pk_persona}
    return contexto