from api_biblioteca.models import *
from api_biblioteca.serializers import *
from rest_framework import status, request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    # queryset = TblLivro.objects.filter('ID_autor'==@param_arg)
    queryset = TblLivro.objects.all()
    serializer_class = LivroSerializer

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = TblAutores.objects.all()
    serializer_class = AutoresSerializer

class EditorasViewSet(viewsets.ModelViewSet):
    queryset = TblEditoras.objects.all()
    serializer_class = EditorasSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = TblImagefield.objects.all()
    serializer_class = ImagesSerializer