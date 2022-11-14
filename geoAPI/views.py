from django.shortcuts import render
from rest_framework import viewsets
from geoAPI.serialiser import AddressSerializer
from geoAPI.models import Address

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class =AddressSerializer 
    
