from rest_framework import serializers 
from usuarios.models import Usuarios 
 
class UsuariosSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Usuarios
    fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'descricao']
  
    extra_kwargs = {
    'password': {'write_only': True, 'required': False}
    }

  def create(self, validated_data):
    user = Usuarios.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        first_name=validated_data.get('first_name', ''),
        last_name=validated_data.get('last_name', ''),
        descricao=validated_data.get('descricao', ''),
    )
    return user
  
  def update(self, instance, validated_data):
      password = validated_data.pop('password', None)
      for attr, value in validated_data.items():
          setattr(instance, attr, value)
      if password:
          instance.set_password(password)
      instance.save()
      return instance