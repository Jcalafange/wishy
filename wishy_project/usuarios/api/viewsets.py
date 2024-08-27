from rest_framework import viewsets 
from .serializers import UsuariosSerializer
from usuarios.models import Usuarios 
 
class UsuariosViewSet(viewsets.ModelViewSet): 
  serializer_class = UsuariosSerializer 
  queryset = Usuarios.objects.all()