from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Credencial
from .serializer import CredencialSerializer

# Create your views here.
def index(request):
    return HttpResponse("si entro")

class CredencialAPI(viewsets.ModelViewSet):
    queryset = Credencial.objects.all()
    serializer_class = CredencialSerializer