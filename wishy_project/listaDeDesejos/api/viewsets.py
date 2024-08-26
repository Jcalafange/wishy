from rest_framework import viewsets 
from .serializers import ListaDeDesejosSerializer, PresenteSerializer
from ..models import ListaDeDesejos, Presente
 
class ListaDeDesejosViewSet(viewsets.ModelViewSet): 
  serializer_class = ListaDeDesejosSerializer 
  queryset = ListaDeDesejos.objects.all()

class PresenteViewSet(viewsets.ModelViewSet):
  queryset = Presente.objects.all()
  serializer_class = PresenteSerializer