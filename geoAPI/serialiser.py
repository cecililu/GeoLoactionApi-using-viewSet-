from rest_framework import serializers
from geoAPI.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="geoAPI:user-detail")
    class Meta:
        model=User       
        fields = ('url','first_name')
        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        
