from django.urls import (path, include)
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet

app_name = 'authentication'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='User')

urlpatterns = (path('rest/', include(router.urls)),
               path('rest/auth/token', obtain_auth_token, name='token_auth'))
