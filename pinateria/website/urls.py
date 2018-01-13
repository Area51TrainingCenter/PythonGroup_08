from django.urls import path

from website.views import Portada, Buscar, Registro, Logout

urlpatterns = [
    path('buscador/', Buscar.as_view(), name='buscar'),
    path('registro/', Registro.as_view(), name='registro'),

    path('logout/', Logout.as_view(), name='logout'),

    path('', Portada.as_view(), name='portada')
]
