from django.shortcuts import render

# Create your views here.


def entrar(Request):
    return render(Request, 'core/login.html')

def inicial(Request):
    return render(Request, 'core/inicial.html')

def cadastrar(Request):
    return render(Request, 'core/cadastro.html')