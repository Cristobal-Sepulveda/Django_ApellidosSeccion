from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm

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

def form_login(request):
    return render(request, 'form_login.html')

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

