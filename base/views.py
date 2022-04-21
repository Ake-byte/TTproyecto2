from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Registro
from .serializers import RegistroSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/registros/',
        '/api/registros/crear/',

        '/api/registros/<id>/',

        '/api/registros/actualizar/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def getRegistros(request):
    registros = Registro.objects.all()
    serializer = RegistroSerializer(registros, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRegistro(request, pk):
    registro = Registro.objects.get(_id=pk)
    serializer = RegistroSerializer(registro, many=False)

    return Response(serializer.data)