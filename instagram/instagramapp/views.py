from django.shortcuts import render

# Create your views here.

def registrar(request):
    return render(request, 'Registro.html')

def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
