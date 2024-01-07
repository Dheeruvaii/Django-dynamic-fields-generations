from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import  APIView
from .models import *
from .serializer import *
# Create your views here.
class AuthViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializers
    