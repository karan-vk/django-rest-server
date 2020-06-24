from django.shortcuts import render
from .sereializers import CustomerSerializer
from rest_framework import viewsets
from .models import Customer as Cus



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Cus.objects.all()
    serializer_class = CustomerSerializer

# Create your views here.
