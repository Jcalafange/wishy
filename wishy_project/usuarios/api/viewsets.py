from rest_framework import viewsets 
from .serializers import UsuariosSerializer
from usuarios import models 
 
class UsuariosViewSet(viewsets.ModelViewSet): 
  serializer_class = UsuariosSerializer 
  queryset = models.Usuarios.objects.all()