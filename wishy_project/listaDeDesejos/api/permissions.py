from rest_framework import permissions
from listaDeDesejos.models import Presente

class IsOwnerOfList(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.lista.usuario == request.user