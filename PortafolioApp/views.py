from django.shortcuts import render

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
    return render(request, 'PortafolioApp/productos.html')

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
    return render(request, 'PortafolioApp/Coaniquem.html')

def renderDiscapacitados(request):
    return render(request, 'PortafolioApp/Discapacitados.html')
