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