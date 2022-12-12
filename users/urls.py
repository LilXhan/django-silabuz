from django.urls import path
# django tiene un template preparado para el login
# es decir nos provee de la clase LoginView para poder mostrar el formulario inicio de sesion
from django.contrib.auth.views import LoginView, logout_then_login
from . import views
# Segun el documento de django la url correcta para que funcione debe ser accounts/login

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/register', views.RegisterForm.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout')

]



"""
    Login View
    va a buscar el archivo registration/login
    template_name = 'registration/login'
    Esta clase recibe 2 cosas username y password
    Dentro de la clase va a verificar que el usernmae y el password
    ingresados sean correctos

    Para que esto funcione se deben seguir algunas reglas como:
    1: la url se debe llamar: accounts/login/
    2: El template de login debe estar en la carpeta registration/login.html
"""