from django.shortcuts import render

from PortafolioApp.models import Producto

# Create your views here.

def renderHome(request):
    return render(request, 'PortafolioApp/home.html')

def renderLogin(request):
    return render(request, 'PortafolioApp/login.html')

def renderRegister(request):
    return render(request, 'PortafolioApp/register.html')

def renderEncuestas(request):
    return render(request, 'PortafolioApp/encuestas.html')

def renderProductos(request):
    productos = Producto.objects.using('portafolio').all()  # Obtener todos los productos desde productos_db
    #print(productos)  # Esto imprimirá la lista de productos en la consola donde se está ejecutando tu servidor
    return render(request, 'PortafolioApp/productos.html', {'productos': productos})

def renderContacto(request):
    return render(request, 'PortafolioApp/contacto.html')

def renderCampanas(request):
    return render(request, 'PortafolioApp/campanas.html')

def renderQuienes(request):
    return render(request, 'PortafolioApp/quienes.html')

def renderFunciona(request):
    return render(request, 'PortafolioApp/funciona.html')

def renderSalud(request):
    return render(request, 'PortafolioApp/salud.html')

def renderViviendas(request):
    return render(request, 'PortafolioApp/viviendas.html')

def renderAnimales(request):
    return render(request, 'PortafolioApp/animales.html')

def renderCatastrofes(request):
    return render(request, 'PortafolioApp/catastrofes.html')

def renderCoaniquem(request):
    return render(request, 'PortafolioApp/coaniquem.html')

def renderDiscapacitados(request):
    return render(request, 'PortafolioApp/discapacitados.html')

def renderCarrito(request):
    return render(request, 'PortafolioApp/carrito.html')
