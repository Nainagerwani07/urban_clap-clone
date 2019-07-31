from urban.api.viewsets import UserInformationViewSet,  UserViewSet, ServiceProviderInformationViewSet , AddServiceViewSet , CustomerRequestViewSet
from rest_framework import routers
from django.contrib.auth.models import User


router = routers.DefaultRouter()
router.register('User',UserViewSet)
router.register('UserInformation',UserInformationViewSet)
router.register('ServiceProviderInformation',ServiceProviderInformationViewSet)
router.register('AddService',AddServiceViewSet)
router.register('CustomerRequest',CustomerRequestViewSet)
