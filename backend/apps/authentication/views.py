from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import User
from .permissions import (OwnUpdatePermission, AnyCanCreatePermission)
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated | OwnUpdatePermission | AnyCanCreatePermission]
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class UserRegister(viewsets.mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated | OwnUpdatePermission | AnyCanCreatePermission]
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)