from django.urls import path
from apps.Registro.views import registro, login

urlpatterns = [
    path('registro/', registro),
    path('login/', login),


]