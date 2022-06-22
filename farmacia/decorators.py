from django.http import HttpResponse
from django.shortcuts import redirect

#prohibir acceso a pagina
#funcion como parametro

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:    
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

#usuarios permitidos
def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
        
            group = None
            if request.user.groups.exist():
                group = request.user.group.all()[0].name
            
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('no autorizado')
        return wrapper_func
    return decorator