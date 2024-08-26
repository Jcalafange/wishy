from rest_framework import serializers 
from ..models import ListaDeDesejos, Presente

class PresenteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Presente
    fields = '__all__'

class ListaDeDesejosSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = ListaDeDesejos
    fields = '__all__'          