from django.shortcuts import render, redirect
from .forms import LoginForm, ProductoForm, ClienteForm
from .models import Producto, Cliente, User
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')

def somos(request):
    return render(request, 'somos.html')

def contacto(request):
    return render(request, 'contacto.html')

def modal(request):
    return render(request, 'modal.html')

def login(request):
    if request.method=='GET':
        form = LoginForm()
        username = request.GET["rut"]
        password = request.GET["password1"]
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Login attemp failed.')
            return redirect('login')
    
    return render(request, 'login.html',{'form':form})

def form_login(request):
    if request.method=='POST':
        login_form = LoginForm(request.POST, request.FILES)
        if login_form.is_valid():
            rut_ingresado = request.POST["rut"]
            contraseña_ingresada = request.POST["contraseña"]

            try:
                cliente = Cliente.objects.get(rut=rut_ingresado)
                print(cliente)
                return redirect('index')
            except Cliente.DoesNotExist:
                print("Usuario no Existe")
    else:
        login_form = LoginForm()
    return render(request, 'form_login.html',{'login_form': login_form})

def productos(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'productos.html', datos)   

def form_crear_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        print(producto_form.errors)
        if producto_form.is_valid():
            producto_form.save()        #similar al insert
            return redirect('productos')
    else:
        producto_form = ProductoForm()

    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

def form_mod_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            print('exito')
            formulario.save()
            return redirect('productos')
    print('falle')
    return render(request, 'form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('productos')

def clientes(request) :
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'clientes.html', datos)

def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()        #similar al insert
            return redirect('clientes')
        else:
            print(cliente_form.errors)
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})

def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes')
    return render(request, 'form_mod_cliente.html', datos)

def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('clientes')

