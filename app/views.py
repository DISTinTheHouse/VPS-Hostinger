from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("CODE CANVAS SOLUTIONS APP!")


#CODE CANVAS SOLUTIONS HTML . . .
def index(request):
    return render(request, 'index.html')

def clientes(request):
    return render(request, 'clientes.html')

def faq(request):
    return render(request, 'faq.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def precios(request):
    return render(request, 'precios.html')

#APLICACION DE MUESTRAS PARA CLIENTES . . .
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está registrado')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Usuario registrado con éxito')
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    return render(request, 'test/registro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'test/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

#------------------------------------------