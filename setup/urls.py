
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('admin/', admin.site.urls),
    path('inicial/', views.inicial, name='inicial'),
    path('entrar/', views.entrar, name='entrar'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('principal/', views.principal, name='principal'),
    path('reserva/', views.reserva, name='reserva'),
    path('disponibilidade/', views.disponibilidade, name='disponibilidade'),
    path('minha_reserva/', views.minha_reserva, name='minha_reserva'),
]
