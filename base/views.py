from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .registros import registros

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
    return Response(registros)

@api_view(['GET'])
def getRegistro(request, pk):
    registro = None
    for i in registros:
        if i['_id'] == pk:
            registro = i
            break

    return Response(registro)