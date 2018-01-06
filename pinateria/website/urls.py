from django.urls import path

from website.views import Portada, Buscar

urlpatterns = [
    path('buscador/', Buscar.as_view(), name='buscar'),
    path('', Portada.as_view(), name='portada')
]
