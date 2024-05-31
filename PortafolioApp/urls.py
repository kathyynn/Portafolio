from django.contrib import admin
from django.urls import path
from PortafolioApp.views import renderHome, renderLogin, renderRegister, renderEncuestas, renderProductos

urlpatterns = [
    path('', renderHome),
    path('home', renderHome),
    path('login', renderLogin),
    path('register', renderRegister),
    path('encuestas', renderEncuestas),
    path('productos', renderProductos)
]