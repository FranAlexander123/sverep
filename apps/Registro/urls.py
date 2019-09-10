from django.urls import path
from apps.Registro.views import registro

urlpatterns = [
    path('', registro),
]