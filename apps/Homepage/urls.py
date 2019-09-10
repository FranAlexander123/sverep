from django.urls import path
from apps.Homepage.views import homepage
from apps.Registro.views import registro

urlpatterns = [
    path('', homepage),
    path('hola', registro),
]