from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View

from productos.models import Producto

# class Portada(View):
#     def get(self, request):
#         return HttpResponse('Hola Mundo!')


class Portada(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Portada, self).get_context_data(**kwargs)
        contexto['nombre'] = 'Moisés'
        contexto['productos'] = Producto.objects.only('personaje', 'precio')
        contexto['edad'] = 16
        return contexto


class Buscar(ListView):
    template_name = 'buscar.html'
    model = Producto

    def get_queryset(self):
        termino = self.request.GET.get('termino')
        queryset = super(Buscar, self).get_queryset()
        if not termino:
            return queryset.none()
        queryset = queryset.filter(
            Q(personaje__iregex=termino) |
            Q(nombre_comercial__iregex=termino) |
            Q(descripcion__iregex=termino)
        )
        return queryset
