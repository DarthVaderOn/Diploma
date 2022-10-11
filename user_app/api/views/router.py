from rest_framework import routers
from .registration import RegistrationViewSet
from .users import UserViewSet


api_router = routers.DefaultRouter()
api_router.register('user', UserViewSet)
api_router.register('registration', RegistrationViewSet)