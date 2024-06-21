from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Colaborador
from django.contrib.auth.decorators import login_required
# FORMS
from .forms import ColaboradorForm



# def index(request):
#     return HttpResponse("CODE CANVAS SOLUTIONS APP!")


#CODE CANVAS SOLUTIONS HTML . . .
@login_required(login_url="login")
def index(request):
    colaborador = Colaborador.objects.get(correo=request.user.email)
    return render(request, 'index.html', {'colaborador': colaborador})

def clientes(request):
    return render(request, 'clientes.html')

def faq(request):
    return render(request, 'faq.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def precios(request):
    return render(request, 'precios.html')

#--------------------------------------------
""" def register(request):
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
 """
#-----------------------------------------
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
                try:
                    colaborador = Colaborador.objects.get(correo=email)
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, 'Usuario registrado con éxito')
                    return redirect('login')
                except Colaborador.DoesNotExist:
                    messages.error(request, 'No estás autorizado para registrarte. Contacta al administrador.')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    return render(request, 'test/registro.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, introduce tanto el nombre de usuario como la contraseña.')
            return render(request, 'test/login.html')

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
# -- PERFIL Y CONFIGURACIÓNES --

@login_required
def perfil_view(request):
    colaborador = Colaborador.objects.get(correo=request.user.email)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('perfil')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'profile/perfil.html', {'form': form, 'colaborador': colaborador, 'user': request.user})
