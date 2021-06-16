from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Pilot
from .serializers import PilotSerializer
# Create your views here.


@csrf_exempt
def pilot_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pilot = Pilot.objects.all()
        serializer = PilotSerializer(pilot, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PilotSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pilot_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code pilot.
    """
    try:
        pilot = Pilot.objects.get(pk=pk)
    except Pilot.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PilotSerializer(pilot)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PilotSerializer(pilot, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pilot.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def pilot_detail(request, pk):
    """
    Retrieve, update or delete a code pilot.
    """
    try:
        pilot = Pilot.objects.get(pk=pk)
    except Pilot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PilotSerializer(pilot)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PilotSerializer(pilot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pilot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
