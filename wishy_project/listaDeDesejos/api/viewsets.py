from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets 
from .serializers import ListaDeDesejosSerializer, PresenteSerializer
from ..models import ListaDeDesejos, Presente
 
class ListaDeDesejosViewSet(viewsets.ModelViewSet): 
  serializer_class = ListaDeDesejosSerializer 
  queryset = ListaDeDesejos.objects.all()

  @action(detail=True, methods=['post'])
  def adicionar_presente(self, request, pk=None):
      lista = self.get_object()
      serializer = PresenteSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save(lista=lista)
          return Response(serializer.data)
      return Response(serializer.errors, status=400)
  
  @action(detail=True, methods=['get'])
  def presentes(self, request, pk=None):
      lista = self.get_object()
      presentes = lista.presentes.all()
      serializer = PresenteSerializer(presentes, many=True)
      return Response(serializer.data)

class PresenteViewSet(viewsets.ModelViewSet):
  queryset = Presente.objects.all()
  serializer_class = PresenteSerializer