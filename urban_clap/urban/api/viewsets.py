from urban.models import UserInformation , ServiceProviderInformation ,AddService ,CustomerRequest , User
from .serializers import UserSerializer, UserInformationSerializer , ServiceProviderInformationSerializer , AddServiceSerializer , CustomerRequestSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer

class ServiceProviderInformationViewSet(viewsets.ModelViewSet):
    queryset = ServiceProviderInformation.objects.all()
    serializer_class = ServiceProviderInformationSerializer


class AddServiceViewSet(viewsets.ModelViewSet):
    queryset = AddService.objects.all()
    serializer_class = AddServiceSerializer


class CustomerRequestViewSet(viewsets.ModelViewSet):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer
