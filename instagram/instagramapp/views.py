from django.shortcuts import render

# Create your views here.

def registrar(request):
    return render(request, 'Registro.html')


def crear_usuario( request ):
    email = request.POST['email']
    print (request.POST[ 'email' ])
    print (request.POST[ 'name' ])
    name = request.POST['name']
    print (request.POST[ 'user' ])
    name = request.POST['user']
    print (request.POST[ 'password' ])
    name = request.POST['password']

    return render(request, 'Registro.html')

def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
