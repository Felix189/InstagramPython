from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
# Create your views here.

def registrar(request):
    return render(request, 'Registro.html')


def crear_usuario( request ):
    email = request.POST['email']
    print (request.POST[ 'email' ])
    name = request.POST['name']
    print (request.POST[ 'name' ])
    user = request.POST['user']
    print (request.POST[ 'user' ])
    password = request.POST['password']
    print (request.POST[ 'password' ])
    user1=User.objects.create_user (username = user, email = email, first_name = name, password = password)

    myUser = MiUsuario ( usuario = user1)
    myUser.save()
    print (user1)
    print (user1.password)

    return redirect ('login')

    return render(request, 'Registro.html')

def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
