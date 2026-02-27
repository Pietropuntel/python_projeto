
from django.contrib import admin
from django.urls import path
from core import views
from core.views import cadastrar, inicial, entrar, primeira, principal


urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicial", inicial, name= "inicial"),
    path("entrar", entrar, name= "entrar"),
    path("cadastro", cadastrar, name="cadastro"),
    path("principal", principal, name= "principal"),
    path('reserva', views.reserva, name='reserva'),
    path('disponibilidade', views.disponibilidade, name='disponibilidade'),
    path('minha_reserva', views.minha_reserva, name='minha_reserva'),

    path('principal/', views.principal, name='principal'),
]

