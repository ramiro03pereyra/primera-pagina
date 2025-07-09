from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Proveedor, Pedido
from .forms import ProductoForm, ProveedorForm, PedidoForm

# Create your views here.
def inicio(request):
    return render(request, "productos/inicio.html")#listo



def lista_productos_template(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista_productos.html", {"productos": productos})

def cargar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = Producto(
                nombre=form.cleaned_data['nombre'],
                precio=form.cleaned_data['precio'],
                fecha_vencimiento=form.cleaned_data['fecha_vencimiento']
            )
            nuevo_producto.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'productos/cargar-producto.html', {'form': form})



def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "productos/lista_proveedores.html", {"proveedores": proveedores})#listo

def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            nuevo_proveedor = Proveedor(
                nombre=form.cleaned_data["nombre"],
                direccion=form.cleaned_data["direccion"],
                telefono=form.cleaned_data["telefono"]
            )
            nuevo_proveedor.save()
            return redirect("lista_proveedores")
    else:
        form = ProveedorForm()
    return render(request, "productos/form_proveedor.html", {"form": form})#listo

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "productos/lista_pedidos.html", {"pedidos": pedidos})#listo



def crear_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.total = 0
            pedido.save()
            form.save_m2m()
            # Calcular total
            total = sum([p.precio for p in pedido.productos.all()])
            pedido.total = total
            pedido.save()
            return redirect("lista_pedidos")
    else:
        form = PedidoForm()

    return render(request, "productos/form_pedido.html", {"form": form})