from rest_framework import serializers
# from django.core import serializers as srl # Esse mundo é pequeno demais pra dois serializers
from api_biblioteca.models import *
from django.contrib.auth.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblLivro
        fields = '__all__'

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAutores
        fields = '__all__'

class EditorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblEditoras 
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblImagefield 
        fields = '__all__'