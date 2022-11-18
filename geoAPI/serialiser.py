from rest_framework import serializers
from geoAPI.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="geoAPI:user-detail")
    class Meta:
        model=User       
        fields = '__all__'
        
class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        
