from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



from geoAPI.serialiser import AddressSerializer,UserSerializer
from geoAPI.models import Address
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class =AddressSerializer 
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
 #userViewsets
class UserViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=User.objects.all()
        serialzer=UserSerializer(queryset,many=True)
        return Response(serialzer.data)
    
    def retrieve(self,request,pk=None):
        queryset=User.objects.all() 
        user=get_object_or_404(queryset,id=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    def delete(self,request,pk=None):
        deleteuser=User.objects.get(pk=pk)
        deleteuser.delete()
        return Response({'msg':'Deleted'})
        
        