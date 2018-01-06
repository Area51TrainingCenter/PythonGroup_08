from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View


# class Portada(View):
#     def get(self, request):
#         return HttpResponse('Hola Mundo!')


class Portada(TemplateView):
    template_name = 'index.html'
