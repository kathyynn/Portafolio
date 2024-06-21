from django.contrib import admin
from django.urls import path
from PortafolioApp.views import renderHome, renderLogin, renderRegister, renderEncuestas, renderProductos, renderCampanas, renderContacto, renderQuienes, renderFunciona, renderSalud, renderViviendas, renderDiscapacitados, renderCoaniquem, renderCatastrofes, renderAnimales, renderCarrito

urlpatterns = [
    path('', renderHome),
    path('home', renderHome),
    path('login', renderLogin),
    path('register', renderRegister),
    path('encuestas', renderEncuestas),
    path('productos', renderProductos),
    path('campanas', renderCampanas),
    path('contacto', renderContacto),
    path('quienes', renderQuienes),
    path('funciona', renderFunciona),
    path('salud', renderSalud),
    path('animales', renderAnimales),
    path('catastrofes', renderCatastrofes),
    path('coaniquem', renderCoaniquem),
    path('discapacitados', renderDiscapacitados),
    path('viviendas', renderViviendas),
    path('carrito', renderCarrito)


]