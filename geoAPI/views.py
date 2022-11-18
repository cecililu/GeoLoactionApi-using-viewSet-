from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from django.contrib.auth.models import User

from geoAPI.serialiser import AddressSerializer,UserSerializer
from geoAPI.models import Address

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class =AddressSerializer 

 #userViewsets   

class UserViewSet(viewsets.ViewSet):
    
    def list(self,request):
        queryset=User.objects.all()
        serialzer=UserSerializer(queryset,many=True)
        return Response(serialzer.data)