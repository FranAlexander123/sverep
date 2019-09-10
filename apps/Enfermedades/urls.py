from django.urls import path
from apps.Enfermedades.views import enfermedad1

urlpatterns = [
    path('', enfermedad1),
]