from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, ProgrammingLanguage
from .serializer import DogSerializer, ProgrammingLanguageSerializer

# Create your views here.
# Base views


def index(request):
    return render(request, 'index.html')

# View sets


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer

