from rest_framework import serializers
from django.contrib.auth.models import User
from urban.models import  UserInformation , ServiceProviderInformation ,AddService ,CustomerRequest


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username','email','password']

class UserInformationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserInformation
		fields = ['user_type','user']


class ServiceProviderInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceProviderInformation
        fields = ['user_type','user']


class AddServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddService
        fields = ['add_services','s_provider','user']        


class CustomerRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = ['status','addservice','user','review']        
