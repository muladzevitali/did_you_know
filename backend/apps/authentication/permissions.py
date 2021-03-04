from rest_framework import permissions


class OwnUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # check that its an update request and user is modifying his resource only
        if view.action == 'update' and view.kwargs['id'] != request.user.id:
            return False
        return True


class AnyCanCreatePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        # check that its an update request and user is modifying his resource only
        if view.action == 'create':
            return True
