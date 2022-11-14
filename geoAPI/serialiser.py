from rest_framework import serializers
from geoAPI.models import *

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
         