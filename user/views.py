from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for listing or retrieving users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

