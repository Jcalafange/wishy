from rest_framework import serializers 
from ..models import ListaDeDesejos, Presente

class PresenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presente
        fields = ['id', 'nome', 'preco', 'querometro', 'descricao_presente', 'link']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Presente.objects.create(**validated_data)

class ListaDeDesejosSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = ListaDeDesejos
    fields = '__all__'          