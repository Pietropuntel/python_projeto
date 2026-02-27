from django.shortcuts import render

# Create your views here.


def entrar(Request):
    return render(Request, 'core/inicial.html')

def inicial(Request):
    return render(Request, 'core/inicial.html')

def cadastrar(Request):
    return render(Request, 'core/cadastro.html')

def primeira (Request):
     return render(Request, 'core/primeira.html')

def principal (Request):
    return render(Request, 'core/pg_principal.html')

def reserva(request):
    return render(request, 'core/reserva.html')

def disponibilidade(request):
    return render(request, 'disponibilidade.html')

def minha_reserva(request):
    return render(request, 'minha_reserva.html')