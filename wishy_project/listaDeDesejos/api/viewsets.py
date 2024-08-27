from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ListaDeDesejosSerializer, PresenteSerializer
from ..models import ListaDeDesejos, Presente
from .permissions import IsOwnerOfList
 
class ListaDeDesejosViewSet(viewsets.ModelViewSet): 
    serializer_class = ListaDeDesejosSerializer 
    queryset = ListaDeDesejos.objects.all()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def adicionar_presente(self, request, pk=None):
        lista = self.get_object()
        serializer = PresenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(lista=lista)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
  
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def presentes(self, request, pk=None):
        lista = self.get_object()
        presentes = lista.presentes.all()
        serializer = PresenteSerializer(presentes, many=True)
        return Response(serializer.data)

class PresenteViewSet(viewsets.ModelViewSet):
    queryset = Presente.objects.all()
    serializer_class = PresenteSerializer
    permission_classes = [IsOwnerOfList]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOfList]
        return super().get_permissions()