
from django.contrib import admin
from django.urls import path
from core.views import cadastrar, inicial, entrar, primeira


urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicial", inicial, name= "inicial"),
    path("entrar", entrar, name= "entrar"),
    path("cadastro", cadastrar, name="cadastro"),
    path("", primeira)
]
